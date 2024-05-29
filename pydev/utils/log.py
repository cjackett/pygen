import logging
from enum import Enum

import rich.logging

# Global Rich (console) handler
RICH_HANDLER = rich.logging.RichHandler(
    level=logging.WARNING,
    log_time_format="%Y-%m-%d %H:%M:%S,%f",
    markup=True,
    show_path=True,
    rich_tracebacks=True,
    tracebacks_show_locals=False,
)


def get_logger(name: str, level: int = logging.DEBUG) -> logging.Logger:
    """
    Get a logger with a given name and level.

    Args:
        name: The name of the logger.
        level: The level of the logger.

    Returns:
        A logger.
    """
    # Create the logger and add the Rich handler
    logger = logging.Logger(name, level)
    logger.addHandler(RICH_HANDLER)

    return logger


def get_rich_handler() -> rich.logging.RichHandler:
    """
    Get the global Rich handler.

    Returns:
        The Rich handler.
    """
    return RICH_HANDLER


class LogLevel(str, Enum):
    """
    Enumerated log levels for CLI.
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class LogMixin:
    """
    Mixin for logging. Adds a `logger` property that provides a `logging.Logger` ad-hoc using the class name.
    """

    @property
    def logger(self) -> logging.Logger:
        # Lazy initialization
        if not hasattr(self, "_logger"):
            self._logger = get_logger(self.__class__.__name__)
            # Add NullHandler to avoid logs on stdout by default
            self._logger.addHandler(logging.NullHandler())
        return self._logger
