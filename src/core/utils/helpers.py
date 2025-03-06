# 

import os
import sys

import json
import yaml
import dill 

import pandas as pd
import streamlit as st

from src.core.exception import BankChurnException




#----------------------------------------------------------------
#------------------------ Json Helpers --------------------------
#----------------------------------------------------------------

# Function for reading JSON file from provided path
@st.cache_resource(allow_output_mutation=True)
def read_json(file_path: str) -> dict:
    """
    Read a JSON file and return its content as a dictionary.

    Parameters:
    file_path (str): The path to the JSON file to be read.

    Returns:
    dict: The content of the JSON file as a dictionary.

    Raises:
    BankChurnException: If an error occurs while reading the JSON file.
    """
    try:
        with open(file_path, "r") as json_file:
            return json.load(json_file)

    except FileNotFoundError:
        raise BankChurnException(f"Report file not found at {file_path}.", sys)

    except json.JSONDecodeError:
        raise BankChurnException("Failed to decode the report JSON file.", sys)

    except Exception as e:
        raise BankChurnException(f"Error in load_report: {str(e)}", sys) from e
    

# Function to write JSON file to provided path
@staticmethod
def write_json(file_path: str, data, replace: bool = False) -> None:
    """
    Write a dictionary to a JSON file.
    
    Parameters:
    file_path (str): The path to the JSON file to be written.
    data (object): The dictionary to be written to the JSON file.
    replace (bool, optional): If True, overwrite the file if it already exists. Defaults to False.
    
    Raises:
    BankChurnException: If an error occurs while writing the JSON file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    
    except Exception as e:
        raise BankChurnException(e, sys) from e



#----------------------------------------------------------------
#------------------------ Yaml Helpers --------------------------
#----------------------------------------------------------------

# Function for Reading Yaml file from provided path
@st.cache_resource(allow_output_mutation=True)
def read_yaml(file_path: str) -> dict:
    """
    Read a YAML file and return its content as a dictionary.

    Parameters:
    file_path (str): The path to the YAML file to be read.

    Returns:
    dict: The content of the YAML file as a dictionary.

    Raises:
    BankChurnException: If an error occurs while reading the YAML file.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise BankChurnException(e, sys) from e
    

# Function to write Yaml file to provided path
@staticmethod
def write_yaml(file_path: str, data, replace: bool = False) -> None:
    """
    Write a dictionary to a YAML file.
    
    Parameters:
    file_path (str): The path to the YAML file to be written.
    content (object): The dictionary to be written to the YAML file.
    replace (bool, optional): If True, overwrite the file if it already exists. Defaults to False.
    
    Raises:
    BankChurnException: If an error occurs while writing the YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w") as file:
            yaml.dump(data, file)
    
    except Exception as e:
        raise BankChurnException(e, sys) from e



#----------------------------------------------------------------
#------------------------ Data Helpers --------------------------
#----------------------------------------------------------------

# Function for Reading data from a file
@st.cache_resource(allow_output_mutation=True)
def read_data(file_path: str) -> pd.DataFrame:
    """
    Read data from a CSV file and return it as a DataFrame.

    Parameters:
    file_path (str): The path to the YAML file to be read.

    Returns:
    DataFrame: A DataFrame containing the data from the CSV file.

    Raises:
    BankChurnException: If an error occurs while reading the YAML file.
    """
    try:
        dataframe = pd.read_csv(file_path)
       
        return dataframe
    
    except Exception as e:
        raise BankChurnException(f"Error reading data from {file_path}: {str(e)}", sys) from e


# Function for saving data to a file
@staticmethod
def save_data(dataframe: pd.DataFrame, file_path: str) -> None:
    """
    Save the given DataFrame to a CSV file at the specified file path.

    Parameters:
    DataFrame: A DataFrame containing the data from the CSV file.
    file_path: The file path where the DataFrame will be saved.

    Raises:
    BankChurnException: If an error occurs while reading the YAML file.
    """
    try:
        # Ensure the directory exists
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Save the DataFrame to a CSV file
        dataframe.to_csv(file_path, index=False, header=True)
    
    except Exception as e:
        raise BankChurnException(f"Error saving data to {file_path}: {str(e)}", sys) from e
    


#----------------------------------------------------------------
#----------------------- Object Helpers -------------------------
#----------------------------------------------------------------
# Function for saving the object
@staticmethod
def save_object(file_path: str, obj: object) -> None:
    """
    Save an object to a file using the dill module.
    
    Parameters:
    file_path (str): The path to the file to be written.
    obj (object): The object to be written to the file.
    
    Raises:
    BankChurnException: If an error occurs while saving the object.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise BankChurnException(e, sys) from e
    

# Function for loading the object
@st.cache_resource(allow_output_mutation=True)
def load_object(file_path: str) -> object:
    """
    Load an object from a file using the dill module.
    
    Parameters:
    file_path (str): The path to the file containing the object to be loaded.
    
    Returns:
    object: The loaded object from the file.
    
    Raises:
    BankChurnException: If an error occurs while loading the object.
    """
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        return obj

    except Exception as e:
        raise BankChurnException(e, sys) from e
