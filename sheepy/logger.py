import logging

class TestLogger:
    def __init__(self, level=logging.INFO):
        logging.basicConfig(level=level)
        self.logger = logging.getLogger('TestLogger')

    def log(self, message):
        self.logger.info(message)

    def set_level(self, level):
        self.logger.setLevel(level)
