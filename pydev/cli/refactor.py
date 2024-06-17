import typer

from pydev.utils.log import get_logger

logger = get_logger(__name__)

refactor_app = typer.Typer(
    help="Refactor Python code including modules, classes, or functions to improve structure and readability.",
    no_args_is_help=True,
)


@refactor_app.command(name="module")
def refactor_module(module_name: str) -> None:
    """Refactor a module."""
    logger.info(f"Refactoring module: {module_name}")


@refactor_app.command(name="class")
def refactor_class(class_name: str) -> None:
    """Refactor a class."""
    logger.info(f"Refactoring class: {class_name}")


@refactor_app.command(name="function")
def refactor_function(function_name: str) -> None:
    """Refactor a function."""
    logger.info(f"Refactoring function: {function_name}")
