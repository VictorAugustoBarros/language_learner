"""Classe para controle de Logs."""
import logging
import os
import sys
import json


class Logger:
    """Classe de Logger."""

    def __init__(self, name="language_learner"):
        """Construtor da classe."""
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            log_format = "%(asctime)-15s %(levelname)s: %(message)s"
            formatter = logging.Formatter(log_format)

            hdlr = logging.StreamHandler(sys.stdout)
            hdlr.setFormatter(formatter)
            self.logger.addHandler(hdlr)

            log_level = self.get_log_level(os.environ.get("LOG_LEVEL", "INFO"))
            self.logger.setLevel(log_level)

    def get_log_level(self, log_level: str):
        """Busca do log level a partir de uma string.

        Args:
            log_level (str): Log Level
        """
        if log_level.upper() == "DEBUG":
            return logging.DEBUG

        elif log_level.upper() == "INFO":
            return logging.INFO

        elif log_level.upper() == "ERROR":
            return logging.ERROR

        return None

    def info(self, message, **kwargs):
        """Log message in Debug level.

        Args:
            message ():
            **kwargs ():
        """
        message = json.dumps(message, ensure_ascii=False)
        self.logger.info(message, **kwargs)

    def warning(self, message, **kwargs):
        """Logger para nivel WARNING.

        Args:
            message ():
            **kwargs ():
        """
        message = json.dumps(message, ensure_ascii=False)
        self.logger.warning(message, **kwargs)

    def success(self, message, **kwargs):
        """Logger para nivel SUCCESS.

        Args:
            message ():
            **kwargs ():
        """
        message = json.dumps(message, ensure_ascii=False)
        self.logger.info(message, **kwargs)

    def error(self, message, **kwargs):
        """Logger para nivel ERROR.

        Args:
            message ():
            **kwargs ():
        """
        message = json.dumps(message, ensure_ascii=False)
        self.logger.error(message, **kwargs)

    def critical(self, message, **kwargs):
        """Logger para nivel CRITICAL.

        Args:
            message ():
            **kwargs ():
        """
        self.logger.critical(message, **kwargs)

    def debug(self, message: dict, **kwargs):
        """Logger para nivel ERROR.

        Args:
            message (dict):
            **kwargs (dict):
        """
        self.logger.debug(msg=message, **kwargs)
