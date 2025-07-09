import os # this line is added to ensure the file is recognized as a Python module
import sys # sys means system, it is used to get the current system information

import numpy as np # numpy is a library for numerical operations
import dill # dill is used for serializing and deserializing Python objects
import yaml # yaml is used for reading and writing YAML files
from pandas import DataFrame # pandas is a library for data manipulation and analysis
import logging

from mlops_uno.exceptions import MLOpsUnoException # this line imports a custom exception class for handling errors in the MLOpsUno framework
from mlops_uno.logging import logger # this line imports a logger for logging messages in the MLOpsUno framework

def read_yaml_file(file_path: str) -> dict: # this line defines a function to read a YAML file and return its content as a dictionary
    """
    Reads a YAML file and returns its content as a dictionary.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Content of the YAML file.
    """
    try: # this line starts a try block to catch exceptions
        with open(file_path, 'rb') as yaml_file: # open the YAML file in binary read mode
            content = yaml.safe_load(yaml_file) # this line reads the content of the YAML file safely
        return content # this line returns the content of the YAML file as a dictionary
    except Exception as e: # this line catches any exception that occurs during the file reading process
        raise MLOpsUnoException(e, sys) from e # this line raises a custom exception with the caught exception and the system information
    

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes a dictionary to a YAML file.

    Args:
        file_path (str): Path to the YAML file.
        content (dict): Content to write to the YAML file.
    """
    try:
        if replace: # this line checks if the replace flag is set to True
            if os.path.exists(file_path): # this line checks if the file exists
                os.remove(file_path) # this line removes the file if it exists and replace is True
        os.makedirs(os.path.dirname(file_path), exist_ok=True) # this line creates the directory if it does not exist
        with open(file_path, 'w') as file: # open the YAML file in write mode
            yaml.dump(content, file) # this line writes the content to the YAML file
    except Exception as e: # this line catches any exception that occurs during the file writing process
        raise MLOpsUnoException(e, sys) from e # this line raises a custom exception if an error occurs

def load_object(file_path: str) -> object: # this line defines a function to load a serialized Python object from a file
    logging.info("Entered the load_object method of utils") # this line logs the file path from which the object is being loaded
    """
    Loads a Python object from a file.

    Args:
        file_path (str): Path to the file containing the serialized object.

    Returns:
        object: The deserialized Python object.
    """
    try:
        with open(file_path, 'rb') as file_obj: # open the file in binary read mode
            obj = dill.load(file_obj) # this line loads and returns the serialized object
        logging.info("Entered the load_object method of utils")
        return obj # this line returns the loaded object
    
    except Exception as e: # this line catches any exception that occurs during the file loading process
        raise MLOpsUnoException(e, sys) from e # this line raises a custom exception if an error occurs

def save_numpy_array_data(file_path: str, array: np.array): # this line defines a function to save a NumPy array to a file
    """
    Saves a NumPy array to a file.

    Args:
        file_path (str): Path to the file where the array will be saved.
        array (np.ndarray): NumPy array to save.
    """
    try:
        dir_path = os.path.dirname(file_path) # this line gets the directory path from the file path
        os.makedirs(dir_path, exist_ok=True) # this line creates the directory if it does not exist
        with open(file_path, 'wb') as file_obj: # open the file in binary write mode
            np.save(file_path, array) # this line saves the NumPy array to the specified file
            
    except Exception as e: # this line catches any exception that occurs during the file saving process
        raise MLOpsUnoException(e, sys) from e # this line raises a custom exception if an error occurs
    
def load_numpy_array_data(file_path: str) -> np.array: # this line defines a function to load a NumPy array from a file
    """    Loads a NumPy array from a file.
    Args:
        file_path (str): Path to the file containing the NumPy array.
    Returns:
        np.ndarray: The loaded NumPy array.
    """
    try:
        with open(file_path, 'rb') as file_obj: # open the file in binary read mode
            array = np.load(file_obj) # this line loads and returns the NumPy array from the file
        return array # this line returns the loaded NumPy array
    
    except Exception as e: # this line catches any exception that occurs during the file loading process
        raise MLOpsUnoException(e, sys) from e # this line raises a custom exception if an error occurs

def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_obj method of utils") # this line defines a function to save a Python object to a file
    """Saves a Python object to a file.
    Args:
        file_path (str): Path to the file where the object will be saved.
        obj (object): Python object to save.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True) # this line creates the directory if it does not exist
        with open(file_path, 'wb') as file_obj: # open the file in binary write mode
            dill.dump(obj, file_obj) # this line saves the Python object to the specified file
            
    except Exception as e: # this line catches any exception that occurs during the file saving process
        raise MLOpsUnoException(e, sys) from e # this line raises a custom exception if an error occurs

def drop_columns(data_frame: DataFrame, columns: list) -> DataFrame:
    logging.info("Entered drop_columns method of utils")
    """
    Drops specified columns from a DataFrame.

    Args:
        data_frame (DataFrame): The DataFrame from which to drop columns.
        columns (list): List of column names to drop.

    Returns:
        DataFrame: The DataFrame with specified columns dropped.
    """
    try:
        df = df.drop(columns, axis=1) # this line drops the specified columns from the DataFrame
        logging.info("Entered drop_columns method of utils")
        
        return df # this line returns the modified DataFrame without the dropped columns
    except Exception as e: # this line catches any exception that occurs during the column dropping process
        raise MLOpsUnoException(e, sys) from e # this line raises a custom exception if an error occurs