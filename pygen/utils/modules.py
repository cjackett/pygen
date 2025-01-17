import ast
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import typer
from rich.console import Console
from rich.table import Table

from pygen.utils.log import get_logger
from pygen.utils.rich import selection_panel

logger = get_logger(__name__)


def extract_module_name(file_path: Path) -> str:
    """Extract the module name from the file path including .py extension."""
    return file_path.name


def extract_classes(file_path: Path) -> List[str]:
    """Extract classes from a Python file."""

    with file_path.open("r") as file:
        tree = ast.parse(file.read())

    classes = [f"{file_path}:{node.name}()" for node in tree.body if isinstance(node, ast.ClassDef)]
    return classes


def extract_functions(file_path: Path) -> List[str]:
    """Extract functions from a Python file, including functions within classes."""

    def get_functions(node: ast.AST) -> List[str]:
        """Recursively get all function names from the node."""
        functions: List[str] = []
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        for child in ast.iter_child_nodes(node):
            functions.extend(get_functions(child))
        return functions

    with file_path.open("r") as file:
        tree = ast.parse(file.read())

    functions = [f"{file_path}:{node.name}()" for node in tree.body if isinstance(node, ast.FunctionDef)]

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_functions = get_functions(node)
            functions.extend([f"{file_path}:{func_name}()" for func_name in class_functions])

    return functions


def select_from_list(options: List[Path] | List[str], title: str, prompt_message: str) -> str:
    """Prompt the user to select an option from the list using a Rich table for enhanced presentation."""
    console = Console()

    # Sort options alphabetically by path
    options.sort()

    # Determine the width for alignment based on the number of options
    num_width = len(str(len(options)))

    # Create a table without a border and with a styled title
    table = Table(show_header=False, expand=True, box=None)
    table.add_column(style="cyan")
    table.add_column(style="cyan")
    table.add_column(style="cyan")

    # Calculate the number of rows needed
    num_columns = 3
    num_rows = (len(options) + num_columns - 1) // num_columns

    # Add options to the table, increasing down each column
    for row_idx in range(num_rows):
        row = []
        for col_idx in range(num_columns):
            option_idx = row_idx + col_idx * num_rows
            if option_idx < len(options):
                number = str(option_idx + 1).rjust(num_width)
                row.append(f"{number}. {options[option_idx]}")
            else:
                row.append("")  # Fill with an empty string if no more options
        table.add_row(*row)

    console.print(selection_panel(table, f"[bold magenta]{title}[/bold magenta]"))
    choice = typer.prompt(prompt_message)

    try:
        index = int(choice) - 1
        if 0 <= index < len(options):
            return str(options[index])
    except (ValueError, IndexError):
        pass

    typer.echo("Invalid selection.")
    raise typer.Exit()


def get_module_file_list(project_root: Path) -> List[Path]:
    """Get a recursive list of file paths for all Python modules from the project root, excluding empty __init__.py
    files."""
    python_files = []

    for p in project_root.rglob("*.py"):
        if p.name == "__init__.py":
            # Check if __init__.py is empty
            if p.stat().st_size == 0:
                continue  # Skip empty __init__.py files
        python_files.append(p)

    return python_files


def normalise_module_name(module_name: str) -> str:
    """Ensure the module name has a .py extension."""
    if not module_name.endswith(".py"):
        module_name += ".py"
    return module_name


def normalise_class_name(class_name: str) -> str:
    """Ensure the class name does not have trailing parentheses."""
    return class_name.rstrip("()")


def normalise_function_name(function_name: str) -> str:
    """Ensure the function name does not have trailing parentheses."""
    return function_name.rstrip("()")


def get_module_names_from_paths(paths: List[Path]) -> Dict[str, Path]:
    """Extract module names (without .py extension) from a list of paths and map them to their paths."""
    return {path.name: path for path in paths}


def validate_module_name(paths: List[Path], module_name: str) -> Optional[Path]:
    """Check if the module name exists in the list of paths and return its path if found."""
    module_name = normalise_module_name(module_name)
    module_name_to_path = get_module_names_from_paths(paths)
    return module_name_to_path.get(module_name)


def validate_class_name(paths: List[Path], class_name: str) -> Optional[Path]:
    """Check if the class name exists in the module file mapping and return its path if found."""
    class_name = normalise_class_name(class_name)
    for file_path in paths:
        classes = extract_classes(file_path)
        for class_entry in classes:
            if class_name in class_entry:
                return file_path
    return None


def validate_function_name(paths: List[Path], function_name: str) -> Optional[Path]:
    """Check if the function name exists in the module file mapping and return its path if found."""
    function_name = normalise_function_name(function_name)
    for file_path in paths:
        functions = extract_functions(file_path)
        for function_entry in functions:
            if function_name in function_entry:
                return file_path
    return None


def remove_module_docstring(tree: ast.Module) -> ast.Module:
    """Remove the module-level docstring if it exists."""
    if (
        len(tree.body) > 0
        and isinstance(tree.body[0], ast.Expr)
        and isinstance(tree.body[0].value, (ast.Str, ast.Constant))
    ):
        tree.body.pop(0)
    return tree


def get_module_content(file_path: Path, strip: bool = False) -> str:
    """Read the content of the given file, optionally stripping the module-level docstring."""
    if not file_path.exists():
        raise FileNotFoundError(f"File '{file_path}' not found.")

    with file_path.open("r") as file:
        content = file.read()

    if strip:
        try:
            tree = ast.parse(content)
            tree = remove_module_docstring(tree)
            content = ast.unparse(tree)
        except SyntaxError as e:
            print(f"Error parsing {file_path}: {e}")
            return ""

    return content


def remove_class_docstring(node: ast.ClassDef) -> ast.ClassDef:
    """Remove the docstring from a class node if it exists."""
    if (
        len(node.body) > 0
        and isinstance(node.body[0], ast.Expr)
        and isinstance(node.body[0].value, (ast.Str, ast.Constant))
    ):
        node.body.pop(0)
    return node


def find_class_code(node: ast.ClassDef, content: str, strip: bool) -> str:
    """Get the source code of the class node, optionally stripping the docstring."""
    if strip:
        node = remove_class_docstring(node)
    return ast.unparse(node)


def get_class_content(file_path: Path, class_name: str, strip: bool = False) -> str:
    """Extract the text of the specified class from the given file."""
    class_name = normalise_class_name(class_name)
    try:
        with file_path.open("r") as file:
            content = file.read()
            tree = ast.parse(content)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return ""
    except SyntaxError as e:
        print(f"Error parsing {file_path}: {e}")
        return ""

    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return find_class_code(node, content, strip)
    return ""


def remove_function_docstring(node: ast.FunctionDef) -> ast.FunctionDef:
    """Remove the docstring from a function node if it exists."""
    if (
        len(node.body) > 0
        and isinstance(node.body[0], ast.Expr)
        and isinstance(node.body[0].value, (ast.Str, ast.Constant))
    ):
        node.body.pop(0)
    return node


def get_function_code(node: ast.FunctionDef, content: str, strip: bool) -> str:
    """Get the source code of the function node, optionally stripping the docstring."""
    if strip:
        node = remove_function_docstring(node)
    return ast.unparse(node)


def find_function(node: ast.AST, name: str, content: str, strip: bool) -> Optional[str]:
    """Recursively find a function by name in the AST and return its source code."""
    if isinstance(node, ast.FunctionDef) and node.name == name:
        return get_function_code(node, content, strip)
    for child in ast.iter_child_nodes(node):
        result = find_function(child, name, content, strip)
        if result:
            return result
    return None


def get_function_content(file_path: Path, function_name: str, strip: bool = False) -> str:
    """Extract the text of the specified function from the given file."""
    function_name = normalise_function_name(function_name)
    try:
        with file_path.open("r") as file:
            content = file.read()
            tree = ast.parse(content)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return ""
    except SyntaxError as e:
        print(f"Error parsing {file_path}: {e}")
        return ""

    function_text = find_function(tree, function_name, content, strip)
    return function_text if function_text is not None else ""


def get_module_path(project_root: Path, module_name: Optional[str]) -> Path:
    """Get the module name selection and validation."""
    module_file_list = get_module_file_list(project_root)
    if module_name:
        module_name = normalise_module_name(module_name)
        module_paths = [p for p in module_file_list if module_name in p.name]
        if len(module_paths) > 1:
            logger.info(f"Multiple modules found with the name '{module_name}': {[str(p) for p in module_paths]}")
            module_path = Path(select_from_list([str(p) for p in module_paths], "Modules", "Select a module by number"))
        elif module_paths:
            module_path = module_paths[0]
        else:
            logger.warning(f"Module '{module_name}' not found")
            raise typer.Exit()
    else:
        module_path = Path(select_from_list([str(p) for p in module_file_list], "Modules", "Select a module by number"))
    return module_path


def get_class_name_and_path(project_root: Path, class_name: Optional[str]) -> Tuple[Path, str]:
    """Get the class name selection and validation."""
    module_file_list = get_module_file_list(project_root)
    if class_name:
        class_name = normalise_class_name(class_name)
        class_paths = [c for p in module_file_list for c in extract_classes(p) if class_name in c]
        if len(class_paths) > 1:
            logger.info(f"Multiple classes found with the name '{class_name}': {list(class_paths)}")
            class_selection = select_from_list(list(class_paths), "Classes", "Select a class by number")
            class_path_str, class_name = class_selection.split(":")
            class_path = Path(class_path_str)
        elif class_paths:
            class_path_str, class_name = class_paths[0].split(":")
            class_path = Path(class_path_str)
        else:
            logger.warning(f"Class '{class_name}()' not found in any module")
            raise typer.Exit()
    else:
        class_paths_list: List[str] = []
        for file_path in module_file_list:
            classes = extract_classes(file_path)
            class_paths_list.extend(cls for cls in classes)
        class_selection = select_from_list(class_paths_list, "Classes", "Select a class by number")
        class_path_str, class_name = class_selection.split(":")
        class_path = Path(class_path_str)
    return class_path, class_name


def get_function_name_and_path(project_root: Path, function_name: Optional[str]) -> Tuple[Path, str]:
    """Get the function name selection and validation."""
    module_file_list = get_module_file_list(project_root)
    if function_name:
        function_name = normalise_function_name(function_name)
        function_paths = [f for p in module_file_list for f in extract_functions(p) if function_name in f]
        if len(function_paths) > 1:
            logger.info(f"Multiple functions found with the name '{function_name}': {list(function_paths)}")
            function_selection = select_from_list(list(function_paths), "Functions", "Select a function by number")
            function_path_str, function_name = function_selection.split(":")
            function_path = Path(function_path_str)
        elif function_paths:
            function_path_str, function_name = function_paths[0].split(":")
            function_path = Path(function_path_str)
        else:
            logger.warning(f"Function '{function_name}()' not found in any module")
            raise typer.Exit()
    else:
        module_path = Path(select_from_list([str(p) for p in module_file_list], "Modules", "Select a module by number"))
        functions = extract_functions(module_path)
        if not functions:
            logger.warning(f"No functions found in module '{module_path.name}()'")
            raise typer.Exit()
        function_selection = select_from_list(list(functions), "Functions", "Select a function by number")
        function_path_str, function_name = function_selection.split(":")
        function_path = Path(function_path_str)
    return function_path, function_name
