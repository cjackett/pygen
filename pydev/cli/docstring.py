import typer

from pydev.utils.log import get_logger

logger = get_logger(__name__)

docstring_app = typer.Typer(
    help="Generate a docstring for a Python module, class or function.",
    no_args_is_help=True,
)


@docstring_app.command(name="module")
def generate_module_docstring(module_name: str) -> None:
    """Generate a docstring for a module."""
    logger.info(f"Generating a docstring for module: {module_name}")


@docstring_app.command(name="class")
def generate_class_docstring(class_name: str) -> None:
    """Generate a docstring for a class."""
    logger.info(f"Generating a docstring for class: {class_name}")


@docstring_app.command(name="function")
def generate_function_docstring(function_name: str) -> None:
    """Generate a docstring for a function."""
    logger.info(f"Generating a docstring for function: {function_name}")
