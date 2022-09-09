from src.infa.logging.BaseLogging import BaseLogging

from flask import current_app
import logging
import logging.config
import yaml


class CustomFormat:
    def __init__(self) -> None:
        super().__init__()
        grey = "\x1b[38;20m"
        yellow = "\x1b[33;20m"
        red = "\x1b[31;20m"
        bold_red = "\x1b[31;1m"
        reset = "\x1b[0m"
        format = "[%(asctime)s] - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

        self.FORMATS = {
            logging.DEBUG: grey + format + reset,
            logging.INFO: grey + format + reset,
            logging.WARNING: yellow + format + reset,
            logging.ERROR: red + format + reset,
            logging.CRITICAL: bold_red + format + reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class CustomHandler(logging.StreamHandler):
    def __init__(self) -> None:
        pass

    def emit(self, record):
        pass


class Logging(BaseLogging):
    def __init__(self) -> None:
        super().__init__()

        # typeFile

        type = current_app.config["TYPE_LOGGING_FILE"]
        file = current_app.config["LOGGING_FILE"]

        if type == "yaml":
            with open(file=file) as stream:
                config = yaml.load(stream=stream, Loader=yaml.FullLoader)
                logging.config.dictConfig(config=config)
        else:
            # load file logging
            logging.config.fileConfig(file)
        # create Logger
        self.logging = logging.getLogger(current_app.config["LOGGER"])

    def debug(self, message=""):
        self.logging.debug(message)

    def info(self, message=""):
        super().info()
        self.logging.info(message)

    def warning(self, message=""):
        super().warning()
        self.logging.warning(message)

    def error(self, message=""):
        super().error()
        self.logging.error(message)

    def critical(self, message=""):
        super().critical()
        self.logging.critical(message)
