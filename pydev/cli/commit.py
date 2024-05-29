import typer

from pydev.utils.log import get_logger

logger = get_logger(__name__)

commit_app = typer.Typer(
    help="Check the staged changes or generate a commit message.",
    no_args_is_help=True,
)


@commit_app.command(name="check")
def commit_check(module_name: str) -> None:
    """Check the staged changes for anything unusual."""
    logger.info(f"commiting module: {module_name}")


@commit_app.command(name="message")
def commit_message():
    """Generate a commit message for the staged changes."""
    logger.info("Generating commit message")
