import logging

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

def setup_logger(name, log_file):

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger

trade_logger = setup_logger("trade_logger", "logs/trading.log")
error_logger = setup_logger("error_logger", "logs/errors.log")
api_logger = setup_logger("api_logger", "logs/api.log")