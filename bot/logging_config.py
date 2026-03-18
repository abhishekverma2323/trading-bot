from loguru import logger

def setup_logger():
    logger.add("trading_bot.log", rotation="1 MB", level="INFO")
    return logger