import logging


def setup_custom_logger():
    logging.basicConfig(filename='test_execution.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    return logging.getLogger(__name__)
