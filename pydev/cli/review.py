import typer

from pydev.utils.log import get_logger

logger = get_logger(__name__)

review_app = typer.Typer(
    help="Review the codebase, modules, classes, or functions and suggest improvements.",
    no_args_is_help=True,
)


@review_app.command(name="codebase")
def review_codebase() -> None:
    """Review the codebase and suggest improvements."""
    logger.info("Suggesting improvements for the codebase")


@review_app.command(name="module")
def review_module(module_name: str) -> None:
    """Review a module and suggest improvements."""
    logger.info(f"Suggesting improvements for module: {module_name}")


@review_app.command(name="class")
def review_class_(class_name: str) -> None:
    """Review a class and suggest improvements."""
    logger.info(f"Suggesting improvements for class: {class_name}")


@review_app.command(name="function")
def review_function(function_name: str) -> None:
    """Review a function and suggest improvements."""
    logger.info(f"Suggesting improvements for function: {function_name}")
