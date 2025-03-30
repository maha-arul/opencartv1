import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Define log directory and file
        log_dir = os.path.join(os.path.abspath(os.curdir), 'logs')
        log_file = os.path.join(log_dir, 'automation.log')

        # Ensure the logs directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Configure logging
        logger = logging.getLogger(__name__)

        # Avoid duplicate log handlers
        if not logger.hasHandlers():
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.setLevel(logging.DEBUG)

        return logger
