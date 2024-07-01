"""
Rich console output utilities.
"""

from typing import Tuple

from rich.panel import Panel
from rich.progress import BarColumn, ProgressColumn, TaskProgressColumn, TextColumn, TimeRemainingColumn
from rich.table import Table

PYDEV = "[bold][aquamarine3]PyDev[/aquamarine3][/bold]"


def success_panel(message: str, title: str = "Success") -> Panel:
    """
    Create a success panel.

    Args:
        message: The message to display.
        title: The title of the panel.

    Returns:
        A success panel.
    """
    return Panel(message, title=title, title_align="left", border_style="green3")


def warning_panel(message: str, title: str = "Warning") -> Panel:
    """
    Create a warning panel.

    Args:
        message: The message to display.
        title: The title of the panel.

    Returns:
        A warning panel.
    """
    return Panel(message, title=title, title_align="left", border_style="dark_orange")


def error_panel(message: str, title: str = "Error") -> Panel:
    """
    Create an error panel.

    Args:
        message: The message to display.
        title: The title of the panel.

    Returns:
        An error panel.
    """
    return Panel(message, title=title, title_align="left", border_style="red")


def prompt_panel(message: str, title: str = "Prompt") -> Panel:
    """Create a prompt panel with a customisable message and title.

    This function generates a Panel object with the provided message and title. The panel is styled with a cyan border
    and left-aligned title, suitable for displaying prompts or information to the user. The width of the panel is
    automatically adjusted based on the longest line in the message.

    Args:
        - message: The main content to be displayed in the panel.
        - title: The title of the panel. Defaults to "Prompt".

    Returns:
        A Panel object configured with the specified message and title.
    """
    longest_line_length = max(len(line) for line in message.split("\n"))
    panel_width = longest_line_length + 8
    return Panel(message, title="Prompt", title_align="left", border_style="cyan", width=panel_width)


def selection_panel(table: Table, title: str = "Select from list") -> Panel:
    """Create a Panel containing a Table with a customisable title.

    This function wraps the provided Table within a Panel, allowing for a visually appealing presentation of tabular
    data. The Panel includes a customisable title and uses a bright magenta border style for emphasis.

    Args:
        - table: A Table object to be displayed within the Panel.
        - title: A string representing the title of the Panel. Defaults to "Select from list".

    Returns:
        A Panel object containing the provided Table, with the specified title and styling.
    """
    return Panel(table, title=title, title_align="left", border_style="bright_magenta")


def format_command(command_name: str) -> str:
    """
    Format a command for Rich output.

    Args:
        command_name: The name of the command.

    Returns:
        The formatted command.
    """
    return f"[steel_blue3]{command_name}[/steel_blue3]"


def format_entity(entity_name: str) -> str:
    """
    Format an entity for Rich output.

    Args:
        entity_name: The name of the entity.

    Returns:
        The formatted entity.
    """
    return f"[light_pink3]{entity_name}[/light_pink3]"


def get_default_columns() -> Tuple[ProgressColumn, ...]:
    """
    Get the default progress columns.

    Returns:
        The default progress columns.
    """
    return (
        TextColumn("[bold]{task.description}", justify="left"),
        BarColumn(bar_width=None),
        TaskProgressColumn(),
        TimeRemainingColumn(),
    )
