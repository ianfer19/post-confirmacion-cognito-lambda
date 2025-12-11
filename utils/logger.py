import logging

def get_logger(name: str):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        stream = logging.StreamHandler()
        formatter = logging.Formatter(
            '{"level":"%(levelname)s","message":"%(message)s","logger":"%(name)s"}'
        )
        stream.setFormatter(formatter)
        logger.addHandler(stream)
    return logger
