import os
from box.exceptions import BoxValueError  # For handling ConfigBox-related errors
import yaml  # For reading YAML files
from textSummarizer.logging import logger  # Custom logger
from ensure import ensure_annotations  # For enforcing type annotations
from box import ConfigBox  # A dictionary-like object with attribute-style access
from pathlib import Path  # For working with filesystem paths
from typing import Any  # For type hints


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For any other error during file reading.

    Returns:
        ConfigBox: Parsed content of the YAML file.
    """
    try:
        # Open the YAML file and load its content
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Safely loads YAML content
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")  # Log success
            return ConfigBox(content)  # Convert content to ConfigBox for attribute access
    except BoxValueError:  # Raised when ConfigBox encounters an empty file
        raise ValueError("YAML file is empty")
    except Exception as e:  # Handle any other exceptions
        raise e  # Reraise the exception for debugging


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories if they don't already exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): If True, logs each directory creation. Defaults to True.
    """
    for path in path_to_directories:
        # Create the directory and avoid errors if it already exists
        os.makedirs(path, exist_ok=True)
        if verbose:  # Log only if verbose is True
            logger.info(f"Created directory at: {path}")  # Log the created directory


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Calculates and returns the size of a file in kilobytes (KB).

    Args:
        path (Path): Path to the file.

    Returns:
        str: File size formatted as a string in KB.
    """
    # Get file size in bytes, convert to KB, and round it
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"  # Return size as a formatted string


