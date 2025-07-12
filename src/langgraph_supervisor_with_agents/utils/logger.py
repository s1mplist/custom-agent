import logging

def setup_logger(name: str = "langgraph_supervisor", level: int = logging.DEBUG) -> logging.Logger:
    """
    Sets up and returns a logger with the specified name and logging level.

    If the logger does not already have handlers, a StreamHandler with a custom
    formatter is added. The formatter outputs log messages with the timestamp,
    log level, logger name, and message.

    Args:
        name (str): The name of the logger. Defaults to "langgraph_supervisor".
        level (int): The logging level (e.g., logging.DEBUG, logging.INFO). Defaults to logging.DEBUG.

    Returns:
        logging.Logger: The configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger

def get_logger(name: str = "langgraph_supervisor") -> logging.Logger:
    """Retrieve the logger by name without reconfiguring it."""
    return logging.getLogger(name)