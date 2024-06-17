import typer

from pydev.utils.log import get_logger

logger = get_logger(__name__)

git_app = typer.Typer(
    help="Perform Git operations such as checking staged changes, generating commit messages, or creating pull "
    "request messages.",
    no_args_is_help=True,
)


@git_app.command(name="check")
def git_check(module_name: str) -> None:
    """Check the staged changes for anything unusual."""
    logger.info(f"commiting module: {module_name}")


@git_app.command(name="commit")
def git_commit():
    """Generate a commit message for the staged changes."""
    logger.info("Generating commit message")


@git_app.command(name="pr")
def git_pull_request():
    """Generate a pull request message for the diff between two branches."""
    logger.info("Generating pull request message")
