import logging
logging.basicConfig(level = logging.INFO)

if __name__ == "__main__":
    logging.debug("This is a debug message"),
    logging.info("This is an info message"),
    logging.warning("This is an warning message"),
    logging.error("This is an error message"),
    logging.critical("This is a critical message")