from pathlib import Path
from typing import Optional

import typer

from pygen.prompts.tests import get_class_tests_prompt, get_function_tests_prompt, get_module_tests_prompt
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

logger = get_logger(__name__)

tests_app = typer.Typer(
    help="Generate tests for a Python module, class or function.",
    no_args_is_help=True,
)


@tests_app.command(name="module")
def generate_tests_module(
    ctx: typer.Context,
    module_name: Optional[str] = typer.Argument(None, help="Name of the module"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Generate tests for a module."""
    module_path = get_module_path(project_root, module_name)

    try:
        module_content = get_module_content(module_path)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_module_tests_prompt(module_content)
    prompt_llm(ctx, prompt)


@tests_app.command(name="class")
def generate_tests_class(
    ctx: typer.Context,
    class_name: Optional[str] = typer.Argument(None, help="Name of the class"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Generate tests for a class."""
    class_path, class_name = get_class_name_and_path(project_root, class_name)

    try:
        class_content = get_class_content(class_path, class_name)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_class_tests_prompt(class_content)
    prompt_llm(ctx, prompt)


@tests_app.command(name="function")
def generate_tests_function(
    ctx: typer.Context,
    function_name: Optional[str] = typer.Argument(None, help="Name of the function"),
    project_root: Path = typer.Option(Path("."), help="Root directory of the project"),
) -> None:
    """Generate tests for a function."""
    function_path, function_name = get_function_name_and_path(project_root, function_name)

    try:
        function_content = get_function_content(function_path, function_name)
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit()

    prompt = get_function_tests_prompt(function_content)
    prompt_llm(ctx, prompt)
