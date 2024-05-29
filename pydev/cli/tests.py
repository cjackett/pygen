import typer

from pydev.utils.log import get_logger

logger = get_logger(__name__)

tests_app = typer.Typer(
    help="Generate tests for a Python module, class or function.",
    no_args_is_help=True,
)


@tests_app.command(name="module")
def generate_tests_module(module_name: str) -> None:
    """Generate tests for a module."""
    logger.info(f"Generating tests for module: {module_name}")


@tests_app.command(name="class")
def generate_tests_class(class_name: str) -> None:
    """Generate tests for a class."""
    logger.info(f"Generating tests for class: {class_name}")


@tests_app.command(name="function")
def generate_tests_function(function_name: str) -> None:
    """Generate tests for a function."""
    logger.info(f"Generating tests for function: {function_name}")
