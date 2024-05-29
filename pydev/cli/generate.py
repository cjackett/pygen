from typer import Typer

from pydev.cli.docstring import docstring_app
from pydev.cli.tests import tests_app
from pydev.utils.log import get_logger

logger = get_logger(__name__)

generate_app = Typer(
    help="Generate Python tests or docstrings.",
    no_args_is_help=True,
)

generate_app.add_typer(docstring_app, name="docstring")
generate_app.add_typer(tests_app, name="tests")
