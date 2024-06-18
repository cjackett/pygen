from pathlib import Path
from typing import Optional

import typer

from pydev.prompts.docstring import get_class_prompt, get_function_prompt, get_module_prompt
from pydev.utils.llm import prompt_llm
from pydev.utils.log import get_logger
from pydev.utils.modules import (
    extract_class_text,
    extract_classes_and_functions,
    extract_function_text,
    handle_class_selection,
    handle_function_selection,
    handle_module_selection,
    read_file,
)

logger = get_logger(__name__)

docstring_app = typer.Typer(
    help="Generate a docstring for a Python module, class or function.",
    no_args_is_help=True,
)


@docstring_app.command(name="module")
def generate_docstring_module(
    ctx: typer.Context,
    module_name: Optional[str] = typer.Argument(None, help="Name of the module"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Generate a docstring for a module."""
    module_name, module_file_mapping = handle_module_selection(project_root, module_name)

    file_path = module_file_mapping[module_name]
    try:
        module_content = read_file(file_path)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_module_prompt(module_content)
    module_docstring = prompt_llm(ctx, prompt)
    typer.echo(module_docstring)


@docstring_app.command(name="class")
def generate_docstring_class(
    ctx: typer.Context,
    class_name: Optional[str] = typer.Argument(None, help="Name of the class"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Generate a docstring for a class."""
    class_name, module_file_mapping = handle_class_selection(project_root, class_name)

    # Find the file containing the class
    for _, path in module_file_mapping.items():
        if class_name in extract_classes_and_functions(path)["classes"]:
            file_path = path
            break
    else:
        typer.echo(f"Class '{class_name}' not found in any module.")
        raise typer.Exit()

    try:
        class_content = extract_class_text(file_path, class_name)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_class_prompt(class_content)
    class_docstring = prompt_llm(ctx, prompt)
    typer.echo(class_docstring)


@docstring_app.command(name="function")
def generate_docstring_function(
    ctx: typer.Context,
    function_name: Optional[str] = typer.Argument(None, help="Name of the function"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Generate a docstring for a function."""
    function_name, module_name, module_file_mapping = handle_function_selection(project_root, function_name)

    file_path = module_file_mapping[module_name]
    try:
        function_content = extract_function_text(file_path, function_name)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_function_prompt(function_content)
    function_docstring = prompt_llm(ctx, prompt)
    typer.echo(function_docstring)
