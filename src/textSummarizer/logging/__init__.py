import os 
import sys 
import logging

# Define the format for logging messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Specify the directory and file path for logs
log_dir = "logs"  # Directory to store log files
log_filepath = os.path.join(log_dir, "running_logs.log")  # Full log file path
os.makedirs(log_dir, exist_ok=True)



# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Minimum log level to record
    format=logging_str,  # Log message format


    handlers=[
        logging.FileHandler(log_filepath),  # Write logs to a file
        logging.StreamHandler(sys.stdout)  # Print logs to the console
    ]
)

# Create a logger object with a specific name
logger = logging.getLogger("textSummarizerLogger")


# Example usage of the logger
logger.info("Logging setup is complete.")
logger.error("This is an example of an error log.")