import os
from pathlib import Path
import logging

# Configure logging to display messages with a timestamp and message content
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "textSummarizer"

# List of files and directories to be created for the project
list_of_files = [
    ".github/workflows/.gitkeep",  # To ensure the workflows directory is tracked by Git
    f"src/{project_name}/__init__.py",  # Package initialization file
    f"src/{project_name}/components/__init__.py",  # Sub-package for components
    f"src/{project_name}/utils/__init__.py",  # Sub-package for utility functions
    f"src/{project_name}/utils/common.py",  # Utility script
    f"src/{project_name}/logging/__init__.py",  # Logging module
    f"src/{project_name}/config/__init__.py",  # Configuration module
    f"src/{project_name}/config/configuration.py",  # Configuration handling script
    f"src/{project_name}/pipeline/__init__.py",  # Pipeline-related scripts
    f"src/{project_name}/entity/__init__.py",  # Entity definitions (e.g., data classes)
    f"src/{project_name}/constants/__init__.py",  # Constants used in the project
    "config/config.yaml",  # Main configuration file
    "params.yaml",  # Hyperparameter file
    "app.py",  # Entry point for the application
    "main.py",  # Main script for the project
    "Dockerfile",  # For containerization using Docker
    "requirements.txt",  # List of project dependencies
    "setup.py",  # Script to package and distribute the project
    "research/trials.ipynb",  # Notebook for experiments and trials
]

# Iterate through each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path to a Path object for better handling
    filedir, filename = os.path.split(filepath)  # Split into directory and filename

    # Create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Ensure directory exists, avoid errors if already present
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:  # Open the file in write mode
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        # Log if the file already exists and is not empty
        logging.info(f"{filename} already exists")
