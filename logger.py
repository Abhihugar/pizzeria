from loguru import logger


def setup_logger():
    log_file_path = "logs/app.log"  # You can customize the log file name here
    logger.add(
        log_file_path,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: "
               "<8}</level> | <level>{message}</level> -"
               "<cyan>{file}</cyan>:<cyan>{line}</cyan>",
        level="INFO",
        rotation="500 MB",
        retention="7 days",
        colorize=True,  # Enabled
    )
    return logger
