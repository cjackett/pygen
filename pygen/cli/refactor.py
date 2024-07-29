from pathlib import Path
from typing import Optional

import typer
from rich import print  # noqa: A004

from pygen.prompts.refactor import get_function_refactor_prompt
from pygen.prompts.review import get_module_refactor_prompt
from pygen.utils.llm import prompt_llm
from pygen.utils.log import get_logger
from pygen.utils.modules import get_function_name_and_path, get_function_content, get_module_path, get_module_content
from pygen.utils.rich import warning_panel

logger = get_logger(__name__)

refactor_app = typer.Typer(
    help="Refactor Python code including modules, classes, or functions to improve structure and readability.",
    no_args_is_help=True,
)


@refactor_app.command(name="module")
def review_module(
    ctx: typer.Context,
    module_name: Optional[str] = typer.Argument(None, help="Name of the module"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Refactor a module."""
    module_path = get_module_path(project_root, module_name)

    try:
        module_content = get_module_content(module_path)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_module_refactor_prompt(module_content)
    prompt_llm(ctx, prompt)


@refactor_app.command(name="class")
def refactor_class(class_name: str) -> None:
    """Refactor a class."""
    logger.info(f"Refactoring class: {class_name}")
    print(warning_panel("Not yet implemented"))


@refactor_app.command(name="function")
def refactor_function(
    ctx: typer.Context,
    function_name: Optional[str] = typer.Argument(None, help="Name of the function"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Refactor a function."""
    function_path, function_name = get_function_name_and_path(project_root, function_name)

    try:
        function_content = get_function_content(function_path, function_name)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_function_refactor_prompt(function_content)
    prompt_llm(ctx, prompt)
