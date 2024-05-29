import typer

from pydev.utils.log import get_logger

logger = get_logger(__name__)

suggest_app = typer.Typer(
    help="Suggest improvements for the codebase, module, class, or function.",
    no_args_is_help=True,
)


@suggest_app.command(name="structure")
def suggest_structure() -> None:
    """Suggest improvements for the project structure."""
    logger.info("Suggesting improvements for the project structure")


@suggest_app.command(name="codebase")
def suggest_codebase() -> None:
    """Suggest improvements for the codebase."""
    logger.info("Suggesting improvements for the codebase")


@suggest_app.command(name="module")
def suggest_module(module_name: str) -> None:
    """Suggest improvements for a module."""
    logger.info(f"Suggesting improvements for module: {module_name}")


@suggest_app.command(name="class")
def suggest_class_(class_name: str) -> None:
    """Suggest improvements for a class."""
    logger.info(f"Suggesting improvements for class: {class_name}")


@suggest_app.command(name="function")
def suggest_function(function_name: str) -> None:
    """Suggest improvements for a function."""
    logger.info(f"Suggesting improvements for function: {function_name}")
