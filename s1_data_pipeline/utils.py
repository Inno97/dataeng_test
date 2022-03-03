"""
This module contains some useful functions for general uses that I already wrote beforehand.
"""

import os
import pandas as pd
from log import get_logger

log = get_logger()

def get_file_list(path: str) -> list:
    """Gets the List of files from the specified path.

    Args:
        path (str): The specified path.
    Returns:
        The List of files in that path, or None if not found.
    """
    try:
        return os.listdir(path)
    except FileNotFoundError:
        log.critical('Path does not exist: ' + path)
        return None

def is_file_present_in_directory(dir_name: str, filename: str) -> bool:
    """Returns if a file is present in the given directory.

    Args:
        dir_name (str): The directory to look in.
        filename (str): The filename to look for.
    Returns:
        True if present, False otherwise.
    """
    try:
        if filename in get_file_list(dir_name):
            return True
        else:
            return False
    except FileNotFoundError:
        log.critical('Directory not found: ' + dir_name)
        return False

def is_file_present(path: str) -> bool:
    """Returns if a file with the given path exists.

    Args:
        path (str): The path to the file.
    """
    return os.path.exists(path)

def get_csv(path: str) -> pd.DataFrame:
    """Gets the CSV from a given path as a dataframe.

    Args:
        path (str): The path of the CSV file to load.
    Returns:
        The CSV as a dataframe, or None if not found.
    """
    data = None
    try:
        if not is_file_present(path):
            raise FileNotFoundError
        data = pd.read_csv(path)
        log.info('Got CSV file: ' + path)
    except FileNotFoundError:
        log.warn('Csv file does not exist: ' + path)
    except pd.errors.EmptyDataError:
        log.warn('Csv file exists but is empty: ' + path)
    
    return data

def save_csv(data: pd.DataFrame, path: str) -> bool:
    """Saves a dataframe to a CSV given by a path, and returns whether it was successful.

    Args:
        data (dataframe): The dataframe to save.
        path (str): The path to save the dataframe.
    Returns:
        True if save is successful, else False.
    """
    try:
        data.to_csv(path, index=False)
        log.info('Saved to ' + path)
        return True
    except PermissionError:
        log.critical(path + ' cannot be accessed (PermissionError), is the file open somewhere?')
        return False
    except FileNotFoundError:
        log.critical('No such directory for ' + path)
        return False
    except AttributeError:
        log.warn('Trying to save non-existent csv')
        return False

def generate_csv(dir: str, filename: str, data: list, columns: list) -> bool:
    """Generates an empty csv with the given columns.

    Args:
        path (str): The path to save the CSV to.
        filename (str): The filename of the csv (with .csv)
        data (list): The List of Lists of data to convert.
        columns (list): The List of columns that the CSV should have.
    Returns:
        True if the CSV file is created successfully.
    """
    file_path = dir + '\\' + filename
    df = pd.DataFrame(data, columns=columns)
    save_csv(df, file_path)

    return is_file_present_in_directory(dir, filename)
