# MySQL database connection script

import sys

import pandas as pd
from typing import Optional
from sqlalchemy import create_engine

from src.core.exception import HotelBookingException

from src.core.constants.common_constant import (MYSQL_ENGINE_URL,
                                                DATABASE_NAME)



class MySQLConnect:
    """
    Class Name :   MySQLConnect
    Description :   This class establishes a connection to the MySQL database using SQLAlchemy.

    Output      :   Connection to the MySQL database
    On Failure  :   Raises an exception
    """
    engine = None

    def __init__(self) -> None:
        try:
            # Get SQLAlchemy engine URL from environment variable
            
            mysql_engine_url = MYSQL_ENGINE_URL
            if not mysql_engine_url:
                raise Exception("Environment variable 'MYSQL_ENGINE_URL' is not set.")
            
            if MySQLConnect.engine is None:
                # Initialize the SQLAlchemy engine
                MySQLConnect.engine = create_engine(mysql_engine_url)
            
            self.engine = MySQLConnect.engine
        
        except HotelBookingException as e:
            raise HotelBookingException(f"MySQL connection error: {e}", sys)



class HotelBookingData:
    """
    Class Name :   HotelBookingData
    Description :   This class helps to export entire MySQL table data as a pandas DataFrame.

    Output      :   pd.DataFrame containing the entire MySQL table data
    On Failure  :   Raises an exception
    """

    def __init__(self):
        """
        Initializes the MySQL client connection.
        """
        try:
            self.mysql_connect = MySQLConnect()
        except Exception as e:
            raise HotelBookingException(e, sys)

    def export_data_as_dataframe(self, dataset_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Exports the entire table as a pandas DataFrame.
        
        :param dataset_name: Name of the dataset to export.
        :param database_name: Name of the database (optional, defaults to the connection's database).
        :return: pd.DataFrame containing table data.
        """
        try:
            # Use the default database if none is provided
            database_name = database_name or DATABASE_NAME
            
            # Construct the SQL query
            query = f"SELECT * FROM {database_name}.{dataset_name}"

            # Fetch data using SQLAlchemy
            with self.mysql_connect.engine.connect() as connection:
                df = pd.read_sql(query, connection)

            # Replace placeholder values (e.g., "na") with NaN
            df.replace({"na": pd.NA}, inplace=True)
            
            return df
        except Exception as e:
            raise HotelBookingException(e, sys)
