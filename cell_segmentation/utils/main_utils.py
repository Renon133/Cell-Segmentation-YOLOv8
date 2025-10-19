import os.path
import base64
import yaml
import sys

from cell_segmentation.logger import logging
from cell_segmentation.exception import AppException

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    Args:
        file_path (str): The path to the YAML file.
    Returns:
        dict: The contents of the YAML file as a dictionary.
    """
    try:
        with open(file_path, 'r') as yaml_file:
            logging.info(f"Reading YAML file at: {file_path}")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(f"Error reading YAML file at {file_path}: {e}", sys) from e

def write_yaml_file(file_path: str, content: object, replace:bool = False) -> None:
    """
    Writes content to a YAML file.

    Args:
        file_path (str): The path to the YAML file.
        content (object): The dictionary to write to the YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as yaml_file:
            logging.info(f"Writing to YAML file at: {file_path}")
            yaml.dump(content, yaml_file)

    except Exception as e:
        raise AppException(f"Error writing YAML file at {file_path}: {e}", sys) from e

def encode_image_to_base64(image_path: str) -> str:
    """
    Encodes an image file to a base64 string.

    Args:
        image_path (str): The path to the image file.
    Returns:
        str: The base64 encoded string of the image.
    """
    try:
        with open(image_path, 'rb') as image_file:
            logging.info(f"Encoding image at: {image_path} to base64")
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return encoded_string 
    except Exception as e:
        raise AppException(f"Error encoding image at {image_path} to base64: {e}", sys) from e
    
def decode_base64_to_image(base64_string: str, output_path: str) -> None:
    """
    Decodes a base64 string and writes it to an image file.

    Args:
        base64_string (str): The base64 encoded string of the image.
        output_path (str): The path to save the decoded image file.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'wb') as image_file:
            logging.info(f"Decoding base64 string to image at: {output_path}")
            image_file.write(base64.b64decode(base64_string))
            image_file.close()
    except Exception as e:
        raise AppException(f"Error decoding base64 string to image at {output_path}: {e}", sys) from e
    
