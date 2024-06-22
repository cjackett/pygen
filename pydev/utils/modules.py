import ast
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from pydev.utils.log import get_logger

logger = get_logger(__name__)


def list_python_files(directory: Path) -> List[Path]:
    """List all Python files in the given directory and subdirectories, excluding empty __init__.py files."""
    python_files = []

    for p in directory.rglob("*.py"):
        if p.name == "__init__.py":
            # Check if __init__.py is empty
            if p.stat().st_size == 0:
                continue  # Skip empty __init__.py files
        python_files.append(p)

    return python_files


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

    # Wrap the table in a Panel without inner border
    panel = Panel(table, title=f"[bold magenta]{title}[/bold magenta]", border_style="bright_magenta")

    console.print(panel)

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
    """Get a list of file paths for all Python modules from the project root."""
    return list_python_files(project_root)


def normalize_module_name(module_name: str) -> str:
    """Ensure the module name has a .py extension."""
    if not module_name.endswith(".py"):
        module_name += ".py"
    return module_name


def normalize_class_name(class_name: str) -> str:
    """Ensure the class name does not have trailing parentheses."""
    return class_name.rstrip("()")


def normalize_function_name(function_name: str) -> str:
    """Ensure the function name does not have trailing parentheses."""
    return function_name.rstrip("()")


def get_module_names_from_paths(paths: List[Path]) -> Dict[str, Path]:
    """Extract module names (without .py extension) from a list of paths and map them to their paths."""
    return {path.name: path for path in paths}


def validate_module_name(paths: List[Path], module_name: str) -> Optional[Path]:
    """Check if the module name exists in the list of paths and return its path if found."""
    module_name = normalize_module_name(module_name)
    module_name_to_path = get_module_names_from_paths(paths)
    return module_name_to_path.get(module_name)


def validate_class_name(paths: List[Path], class_name: str) -> Optional[Path]:
    """Check if the class name exists in the module file mapping and return its path if found."""
    class_name = normalize_class_name(class_name)
    for file_path in paths:
        classes = extract_classes(file_path)
        for class_entry in classes:
            if class_name in class_entry:
                return file_path
    return None


def validate_function_name(paths: List[Path], function_name: str) -> Optional[Path]:
    """Check if the function name exists in the module file mapping and return its path if found."""
    function_name = normalize_function_name(function_name)
    for file_path in paths:
        functions = extract_functions(file_path)
        for function_entry in functions:
            if function_name in function_entry:
                return file_path
    return None


def read_file(file_path: Path) -> str:
    """Read the content of the given file."""
    if not file_path.exists():
        raise FileNotFoundError(f"File '{file_path}' not found.")
    with file_path.open("r") as file:
        return file.read()


def extract_class_text(file_path: Path, class_name: str) -> str:
    """Extract the text of the specified class from the given file."""
    class_name = normalize_class_name(class_name)
    with file_path.open("r") as file:
        content = file.read()
        tree = ast.parse(content)

    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            class_text = ast.get_source_segment(content, node)
            if class_text is not None:
                return class_text
    return ""


def extract_function_text(file_path: Path, function_name: str) -> str:
    """Extract the text of the specified function from the given file."""
    function_name = normalize_function_name(function_name)
    with file_path.open("r") as file:
        content = file.read()
        tree = ast.parse(content)

    def find_function(node: ast.AST, name: str, content: str) -> Optional[str]:
        """Recursively find a function by name in the AST and return its source code."""
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return ast.get_source_segment(content, node)
        for child in ast.iter_child_nodes(node):
            result = find_function(child, name, content)
            if result:
                return result
        return None

    function_text = find_function(tree, function_name, content)
    return function_text if function_text is not None else ""


def handle_module_selection(project_root: Path, module_name: Optional[str]) -> Path:
    """Handle module name selection and validation."""
    module_file_list = get_module_file_list(project_root)
    if module_name:
        module_name = normalize_module_name(module_name)
        module_path = validate_module_name(module_file_list, module_name)
        if not module_path:
            logger.warning(f"Module '{module_name}' not found")
            raise typer.Exit()
    else:
        module_path = Path(select_from_list([str(p) for p in module_file_list], "Modules", "Select a module by number"))
    return module_path


def handle_class_selection(project_root: Path, class_name: Optional[str]) -> Tuple[Path, str]:
    """Handle class name selection and validation."""
    module_file_list = get_module_file_list(project_root)
    if class_name:
        class_name = normalize_class_name(class_name)
        class_path = validate_class_name(module_file_list, class_name)
        if not class_path:
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


def handle_function_selection(project_root: Path, function_name: Optional[str]) -> Tuple[Path, str]:
    """Handle function name selection and validation."""
    module_file_list = get_module_file_list(project_root)
    if function_name:
        function_name = normalize_function_name(function_name)
        function_path = validate_function_name(module_file_list, function_name)
        if not function_path:
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
