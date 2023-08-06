# coding=utf-8
import logging


def create_logger(logger_name):
    logger = logging.getLogger(logger_name)

    if logger.level == logging.NOTSET:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(thread)d] %(asctime)s %(name)s:%(levelname)s:%(message)s"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)

    return logger


service_log = create_logger("spiderx-lib")
