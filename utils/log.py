import logging


def setup_custom_logger(name=__name__):

    logger = logging.getLogger(name)

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.FileHandler("/Users/marcin94/PycharmProjects/sauce_demo_ui_tests/test_execution.log")
    handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

