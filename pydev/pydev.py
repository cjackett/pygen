import logging
from datetime import datetime

import typer

from pydev.cli.explain import explain_app
from pydev.cli.generate import generate_app
from pydev.cli.git import git_app
from pydev.cli.refactor import refactor_app
from pydev.cli.resolve import resolve_app
from pydev.cli.review import review_app
from pydev.utils.log import LogLevel, get_logger, get_rich_handler
from pydev.utils.rich import PYDEV

current_year = datetime.now().year

__author__ = "Chris Jackett"
__credits__ = [
    "Chris Jackett <chris.jackett@csiro.au>",
]
__license__ = "TBD"
__version__ = "0.0.2"
__maintainer__ = "Chris Jackett"
__email__ = "chris.jackett@csiro.au"
__status__ = "Development"

pydev = typer.Typer(
    name="PyDev",
    help="""PyDev\n
        A Python Development AI Co-pilot""",
    short_help="PyDev",
    no_args_is_help=True,
    pretty_exceptions_show_locals=False,
)

app = typer.Typer()

pydev.add_typer(explain_app, name="explain")
pydev.add_typer(generate_app, name="generate")
pydev.add_typer(git_app, name="git")
pydev.add_typer(refactor_app, name="refactor")
pydev.add_typer(resolve_app, name="resolve")
pydev.add_typer(review_app, name="review")

logger = get_logger(__name__)


@pydev.callback()
def global_options(
    level: LogLevel = typer.Option(LogLevel.INFO, help="Logging level."),
) -> None:
    """
    Global options for Marimba CLI.
    """
    get_rich_handler().setLevel(logging.getLevelName(level.value))
    logger.info(f"Initialised {PYDEV} CLI v{__version__}")


# Subcommands for convert
@pydev.command()
def convert(file_path: str) -> None:
    """Convert various file types into Python code."""
    logger.info(f"Converting file: {file_path}")


# Command for traceback
@pydev.command()
def traceback() -> None:
    """Provide guidance and suggestions to resolve Python traceback errors."""
    logger.info("Provide guidance and suggestions to resolve Python traceback errors.")


if __name__ == "__main__":
    pydev()
