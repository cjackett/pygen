import ast
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import typer


def list_python_files(directory: Path) -> List[Path]:
    """List all Python files in the given directory and subdirectories."""
    return [p for p in directory.rglob("*.py") if p.name != "__init__.py"]


def extract_module_name(file_path: Path) -> str:
    """Extract the module name from the file path including .py extension."""
    return file_path.name


def extract_classes_and_functions(file_path: Path) -> Dict[str, List[str]]:
    """Extract classes and functions from a Python file."""
    with file_path.open("r") as file:
        tree = ast.parse(file.read())

    classes = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
    functions = [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]

    return {"classes": classes, "functions": functions}


def select_from_list(options: List[str], prompt_message: str) -> str:
    """Prompt the user to select an option from the list."""
    for idx, option in enumerate(options, start=1):
        typer.echo(f"{idx}. {option}")
    choice = typer.prompt(prompt_message)
    try:
        index = int(choice) - 1
        if 0 <= index < len(options):
            return options[index]
    except ValueError:
        pass
    typer.echo("Invalid selection.")
    raise typer.Exit()


def get_module_file_mapping(project_root: Path) -> Dict[str, Path]:
    """Get a mapping of module names to their file paths from the project root."""
    python_files = list_python_files(project_root)
    return {extract_module_name(file): file for file in python_files}


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


def validate_module_name(module_file_mapping: Dict[str, Path], module_name: str) -> bool:
    """Check if the module name exists in the module file mapping."""
    module_name = normalize_module_name(module_name)
    return module_name in module_file_mapping


def validate_class_name(module_file_mapping: Dict[str, Path], class_name: str) -> bool:
    """Check if the class name exists in the module file mapping."""
    class_name = normalize_class_name(class_name)
    class_names = []
    for file in module_file_mapping.values():
        class_function_names = extract_classes_and_functions(file)
        class_names.extend(class_function_names["classes"])
    return class_name in class_names


def validate_function_name(module_file_mapping: Dict[str, Path], function_name: str) -> bool:
    """Check if the function name exists in the module file mapping."""
    function_name = normalize_function_name(function_name)
    function_names = []
    for file in module_file_mapping.values():
        class_function_names = extract_classes_and_functions(file)
        function_names.extend(class_function_names["functions"])
    return function_name in function_names


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

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            function_text = ast.get_source_segment(content, node)
            if function_text is not None:
                return function_text
    return ""


def find_function_module(module_file_mapping: Dict[str, Path], function_name: str) -> Optional[str]:
    """Find the module that contains the given function."""
    function_name = normalize_function_name(function_name)
    for module_name, file in module_file_mapping.items():
        class_function_names = extract_classes_and_functions(file)
        if function_name in [normalize_function_name(name) for name in class_function_names["functions"]]:
            return module_name
    return None


# Higher-level functions to encapsulate functionality


def get_module_names_and_mapping(project_root: Path) -> Dict[str, Path]:
    """Get module names and their file paths."""
    return get_module_file_mapping(project_root)


def handle_module_selection(project_root: Path, module_name: Optional[str]) -> Tuple[str, Dict[str, Path]]:
    """Handle module name selection and validation."""
    module_file_mapping = get_module_names_and_mapping(project_root)
    if module_name:
        module_name = normalize_module_name(module_name)
        if not validate_module_name(module_file_mapping, module_name):
            typer.echo(f"Module '{module_name}' not found.")
            raise typer.Exit()
    else:
        module_names = list(module_file_mapping.keys())
        module_name = select_from_list(module_names, "Select a module by number")
    return module_name, module_file_mapping


def handle_class_selection(project_root: Path, class_name: Optional[str]) -> Tuple[str, Dict[str, Path]]:
    """Handle class name selection and validation."""
    module_file_mapping = get_module_names_and_mapping(project_root)
    if class_name:
        class_name = normalize_class_name(class_name)
        if not validate_class_name(module_file_mapping, class_name):
            typer.echo(f"Class '{class_name}' not found.")
            raise typer.Exit()
    else:
        class_names = []
        for file in module_file_mapping.values():
            class_function_names = extract_classes_and_functions(file)
            class_names.extend(class_function_names["classes"])
        class_name = select_from_list(class_names, "Select a class by number")
    return class_name, module_file_mapping


def handle_function_selection(project_root: Path, function_name: Optional[str]) -> Tuple[str, str, Dict[str, Path]]:
    """Handle function name selection and validation."""
    module_file_mapping = get_module_names_and_mapping(project_root)
    if function_name:
        function_name = normalize_function_name(function_name)
        module_name = find_function_module(module_file_mapping, function_name)
        if not module_name:
            typer.echo(f"Function '{function_name}' not found in any module.")
            raise typer.Exit()
    else:
        module_names = list(module_file_mapping.keys())
        module_name = select_from_list(module_names, "Select a module by number")
        function_names = []
        for file in module_file_mapping.values():
            class_function_names = extract_classes_and_functions(file)
            function_names.extend(class_function_names["functions"])
        function_name = select_from_list(function_names, "Select a function by number")
    return function_name, module_name, module_file_mapping
