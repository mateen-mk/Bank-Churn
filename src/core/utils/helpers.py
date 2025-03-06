# Helper functions

import os
import sys

import json
import yaml
import dill 

import pandas as pd
import streamlit as st

from sklearn.model_selection import train_test_split

from src.core.exception import BankChurnException



# ________________________________________
# |                                      |
# |             JSON Helpers             |
# |--------------------------------------|
# | Functions for reading and saving     |
# | JSON data.                           |
# |______________________________________|

@st.cache_resource(allow_output_mutation=True)
@staticmethod
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



# ________________________________________
# |                                      |
# |             YAML Helpers             |
# |--------------------------------------|
# | Functions for reading and saving     |
# | YAML file.                           |
# |______________________________________|

@st.cache_resource(allow_output_mutation=True)
@staticmethod
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



# ________________________________________
# |                                      |
# |             Data Helpers             |
# |--------------------------------------|
# | Functions for reading and saving     |
# | DataFrames.                          |
# |______________________________________|

@st.cache_resource(allow_output_mutation=True)
@staticmethod
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
    


# ________________________________________
# |                                      |
# |            Object Helpers            |
# |--------------------------------------|
# | Functions for loading and saving     |
# | Model/Preprocessor Objects.          |
# |______________________________________|

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
    

@st.cache_resource(allow_output_mutation=True)
@staticmethod
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



# ________________________________________
# |                                      |
# |             Split Helpers            |
# |--------------------------------------|
# | Functions for splitting train and    |
# | test sets, X and y features.         |
# | Data for Data Validation, Model      |
# | Building.                            |
# |______________________________________|

@st.cache_resource(allow_output_mutation=True)
@staticmethod
def split_data(dataframe: pd.DataFrame, test_size: float) -> tuple:
    """
    Method Name: split_data
    Description :   Splits the given DataFrame into three datasets: train, test, and validation.
    
    Input       :   dataframe       -> The input DataFrame (train/test).
                :   test_size       -> The size of the test dataset in floating point format (0.25) 25% of the whole dataframe.
    
    Output      :   tuple           -> A tuple containing the training DataFrame and the testing DataFrame.
    """ 
    try:
        # Split into train and test data
        train_data, test_data = train_test_split(
            dataframe, 
            test_size=test_size,  
            random_state=12, 
            shuffle=True
        )

        return train_data, test_data
    
    except Exception as e:
        raise BankChurnException(f"Error in split_data: {str(e)}", sys) from e


@st.cache_resource(allow_output_mutation=True)
@staticmethod
def separate_features_and_target(dataframe: pd.DataFrame, target_column: str) -> tuple:
    """
    Method Name :   separate_features_and_target
    Description :   Separates independent features and dependent (target) feature from the DataFrame.
    
    Input       :   df              -> The input DataFrame (train/test).
                :   target_column   -> The name of the target column in the DataFrame.
    
    Output      :   tuple           -> A tuple containing the independent features DataFrame and the target feature series.
    """
    try:        
        # Separating independent features (X) and target feature (y)
        X = dataframe.drop(columns=[target_column], axis=1)
        y = dataframe[target_column]
        
        return X, y

    except Exception as e:
        raise BankChurnException(f"Error in separate_features_and_target: {str(e)}", sys) from e


@st.cache_resource(allow_output_mutation=True)
@staticmethod
def train_test_split_for_data_validation(dataframe: pd.DataFrame, test_size: float) -> tuple:
    """
    Perform train-test split on the given DataFrame for data validation.

    :param dataframe: The DataFrame to split.
    :param test_size: The proportion of the dataset to include in the test split.
    :return: A tuple containing the training set and the testing set.
    """
    try:
        train_set, test_set = train_test_split(dataframe, test_size=test_size, random_state=42)
        return train_set, test_set
    except Exception as e:
        raise BankChurnException(e, sys) from e


@st.cache_resource(allow_output_mutation=True)
@staticmethod
def train_test_split_for_model_building(dataframe: pd.DataFrame, test_size: float, target_column: str) -> tuple:
    """
    Perform train-test split on the given DataFrame with stratification for model training.

    :param dataframe: The DataFrame to split.
    :param test_size: The proportion of the dataset to include in the test split.
    :param target_column: The name of the target column to stratify on.
    :return: A tuple containing the training set and the testing set.
    """
    try:
        # Separate the features and the target column
        X = dataframe.drop(columns=[target_column])
        y = dataframe[target_column]

        # Perform train-test split with stratification
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, stratify=y)

        # # Combine the features and target columns back into DataFrames
        # train_set = pd.concat([X_train, y_train], axis=1)
        # test_set = pd.concat([X_test, y_test], axis=1)

        return X_train, X_test, y_train, y_test 
    except Exception as e:
        raise BankChurnException(e, sys) from e


@st.cache_resource(allow_output_mutation=True)
@staticmethod
def train_test_split_for_tuning(X_train: pd.DataFrame, y_train: pd.Series, test_size: float) -> tuple:
    """
    Perform train-test split on the given training data for hyperparameter tuning.

    :param X_train: The training features DataFrame.
    :param y_train: The training target Series.
    :param test_size: The proportion of the dataset to include in the test split.
    :return: A tuple containing the tuning set features and target.
    """
    try:
        # Perform train-test split for hyperparameter tuning
        X_tune, _, y_tune, _ = train_test_split(X_train, y_train, test_size=test_size)
        return X_tune, y_tune
    except Exception as e:
        raise BankChurnException(e, sys) from e
