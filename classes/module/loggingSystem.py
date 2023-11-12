import logging
import os

class Logger:
    _instance = None

    @classmethod
    def getInstance(cls, log_directory=None): # for singleton
        if cls._instance is None:
            cls._instance = cls(log_directory)
        return cls._instance

    def __init__(self, log_directory):
        if Logger._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger._instance = self

            # log file directory path
            self.log_file_path = os.path.join(log_directory, 'game_log.log')

            self.logger = logging.getLogger('coinRapidGame__logger')
            self.logger.setLevel(logging.DEBUG)

            # file handler
            file_handler = logging.FileHandler(self.log_file_path)
            file_handler.setLevel(logging.DEBUG)

            # logging format
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def logGeneral(self, message):
        self.logger.info(message)
    
    def logError(self, message):
        self.logger.error(message)