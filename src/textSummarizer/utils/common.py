import os
from box.exceptions import BoxValueError  # Handles ConfigBox-specific errors
import yaml  # For reading YAML files
from pathlib import Path  # For handling filesystem paths
from box import ConfigBox  # A dictionary-like object with attribute-style access
from typing import Any, List  # For type hints
from textSummarizer.logging import logger  # Custom logger

# Replace 'ensure_annotations' with 'typeguard'
from typeguard import typechecked


@typechecked
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
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)  # Load YAML content safely
            if not content:  # Check if the file is empty
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file '{path_to_yaml}' loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"BoxValueError: {e}")
        raise ValueError("Invalid YAML content")
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise


@typechecked
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@typechecked
def get_size(path: Path) -> str:
    """
    Calculates and returns the size of a file in kilobytes (KB).

    Args:
        path (Path): Path to the file.

    Returns:
        str: File size formatted as a string in KB.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)  # Convert size to KB
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logger.error(f"Error getting size of {path}: {e}")
        raise
