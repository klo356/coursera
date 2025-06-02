import logging

# Setting up the logger and StreamHandler
# Creating a logger

stream_logger = logging.getLogger('stream_logger')
stream_logger.setLevel(logging.DEBUG)  # Set logger to capture all messages from DEBUG level and above

print("len ", len(stream_logger.handlers))
# Ensure no previous handlers are attached
stream_logger.handlers = []

# Creating a StreamHandler
#stream_handler = logging.StreamHandler()
#stream_handler.setLevel(logging.INFO)  # Set handler to display only messages from INFO level and above

# Adding handler to logger
#stream_logger.addHandler(stream_handler)

# Logging messages at different levels
stream_logger.debug("This is a DEBUG message for stream_logger.")
stream_logger.info("This is an INFO message for stream_logger.")
stream_logger.warning("This is a WARNING message for stream_logger.")
stream_logger.error("This is an ERROR message for stream_logger.")
stream_logger.critical("This is a CRITICAL message for stream_logger.")

