import logging

import typer
from rich import print  # noqa: A004

from pygen.cli.explain import explain_app
from pygen.cli.generate import generate_app
from pygen.cli.git import git_app
from pygen.cli.refactor import refactor_app
from pygen.cli.resolve import resolve_app
from pygen.cli.review import review_app
from pygen.llm.client import LLMClient
from pygen.utils.log import LogLevel, get_logger, get_rich_handler
from pygen.utils.rich import PYDEV, error_panel

__author__ = "Chris Jackett"
__credits__ = [
    "Chris Jackett <chris.jackett@csiro.au>",
]
__license__ = "TBD"
__version__ = "0.0.2"
__maintainer__ = "Chris Jackett"
__email__ = "chris.jackett@csiro.au"
__status__ = "Development"

pygen = typer.Typer(
    name="PyDev",
    help="""PyDev\n
        A Python Generative AI Co-pilot""",
    short_help="PyDev",
    no_args_is_help=True,
    pretty_exceptions_show_locals=False,
)

app = typer.Typer()

pygen.add_typer(explain_app, name="explain")
pygen.add_typer(generate_app, name="generate")
pygen.add_typer(git_app, name="git")
pygen.add_typer(refactor_app, name="refactor")
pygen.add_typer(resolve_app, name="resolve")
pygen.add_typer(review_app, name="review")

logger = get_logger(__name__)


@pygen.callback()
def global_options(
    ctx: typer.Context,
    level: LogLevel = typer.Option(LogLevel.INFO, help="Logging level."),
    show: bool = typer.Option(False, help="Show the prompt being sent to the LLM."),
) -> None:
    """
    Global options for Marimba CLI.
    """
    get_rich_handler().setLevel(logging.getLevelName(level.value))
    logger.info(f"Initialised {PYDEV} CLI v{__version__}")

    try:
        llm_client = LLMClient()
        ctx.meta["llm_client"] = llm_client
        ctx.meta["show"] = show
    except EnvironmentError as e:
        logger.error(e)
        print(error_panel(str(e)))
        raise typer.Exit()
    except Exception as e:
        logger.error(e)
        print(error_panel(f"Could not Initialise the LLM client: {e}"))
        raise typer.Exit()


# Subcommands for convert
@pygen.command()
def convert(file_path: str) -> None:
    """Convert various file types into Python code."""
    logger.info(f"Converting file: {file_path}")


# Command for traceback
@pygen.command()
def traceback() -> None:
    """Provide guidance and suggestions to resolve Python traceback errors."""
    logger.info("Provide guidance and suggestions to resolve Python traceback errors.")


if __name__ == "__main__":
    pygen()
