from pathlib import Path
from typing import Optional

import typer
from rich import print  # noqa: A004

from pygen.prompts.review import get_class_review_prompt, get_function_review_prompt, get_module_review_prompt
from pygen.utils.llm import prompt_llm
from pygen.utils.log import get_logger
from pygen.utils.modules import (
    get_class_content,
    get_class_name_and_path,
    get_function_content,
    get_function_name_and_path,
    get_module_content,
    get_module_path,
)
from pygen.utils.rich import warning_panel

logger = get_logger(__name__)

review_app = typer.Typer(
    help="Review the codebase, modules, classes, or functions and suggest improvements.",
    no_args_is_help=True,
)


@review_app.command(name="codebase")
def review_codebase() -> None:
    """Review the codebase and suggest improvements."""
    logger.info("Suggesting improvements for the codebase")
    print(warning_panel("Not yet implemented"))


@review_app.command(name="module")
def review_module(
    ctx: typer.Context,
    module_name: Optional[str] = typer.Argument(None, help="Name of the module"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Review a module and suggest improvements."""
    module_path = get_module_path(project_root, module_name)

    try:
        module_content = get_module_content(module_path)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_module_review_prompt(module_content)
    prompt_llm(ctx, prompt)


@review_app.command(name="class")
def review_class(
    ctx: typer.Context,
    class_name: Optional[str] = typer.Argument(None, help="Name of the class"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Review a class and suggest improvements."""
    class_path, class_name = get_class_name_and_path(project_root, class_name)

    try:
        class_content = get_class_content(class_path, class_name)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_class_review_prompt(class_content)
    prompt_llm(ctx, prompt)


@review_app.command(name="function")
def review_function(
    ctx: typer.Context,
    function_name: Optional[str] = typer.Argument(None, help="Name of the function"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Review a function and suggest improvements."""
    function_path, function_name = get_function_name_and_path(project_root, function_name)

    try:
        function_content = get_function_content(function_path, function_name)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_function_review_prompt(function_content)
    prompt_llm(ctx, prompt)
