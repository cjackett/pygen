import typer
from rich import print  # noqa: A004

from pygen.utils.log import get_logger
from pygen.utils.rich import warning_panel

logger = get_logger(__name__)

explain_app = typer.Typer(
    help="Provide detailed explanations for the Python codebase, module, class, or function.",
    no_args_is_help=True,
)


@explain_app.command(name="codebase")
def explain_codebase():
    """Explain the entire codebase."""
    logger.info("Explaining codebase")
    print(warning_panel("Not yet implemented"))


@explain_app.command(name="module")
def explain_module(module_name: str) -> None:
    """Explain a module."""
    logger.info(f"Explaining module: {module_name}")
    print(warning_panel("Not yet implemented"))


@explain_app.command(name="class")
def explain_class(class_name: str) -> None:
    """Explain a class."""
    logger.info(f"Explaining class: {class_name}")
    print(warning_panel("Not yet implemented"))


@explain_app.command(name="function")
def explain_function(function_name: str) -> None:
    """Explain a function."""
    logger.info(f"Explaining function: {function_name}")
    print(warning_panel("Not yet implemented"))
