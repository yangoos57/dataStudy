import logging


def set_logging():
    logger = logging.getLogger("test")
    stream_handler = logging.StreamHandler()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
