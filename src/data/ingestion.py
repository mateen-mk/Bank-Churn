import os
import sys

from pandas import DataFrame

from src.core.logger import logging
from src.core.exception import BankChurnException

from src.configs.mysql_connection import HotelBookingData
from src.core.entities.config_entity import DataIngestionConfig
from src.core.entities.artifact_entity import DataIngestionArtifact

from src.core.utils.helpers import (read_yaml, save_data) 

from src.core.constants.common import (DATASET_NAME,
                                       SCHEMA_FILE_PATH)




class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        """
        Initialize the DataIngestion class with the provided configuration.

        :param data_ingestion_config: Configuration for data ingestion. If not provided, default configuration is used.

        Raises:
            BankChurnException: If an error occurs during initialization. The exception message and the original error are provided.
        """
        try:
            logging.info("")
            logging.info("- - - Started Data Ingestion Stage: - - -")
            logging.info("- "*50)

            self.dataset_name = DATASET_NAME
            self.data_ingestion_config = data_ingestion_config
            # Read the schema configuration for insignificant columns and other details
            self._schema_config = read_yaml(file_path=SCHEMA_FILE_PATH)
     
        except Exception as e:
            logging.error(f"Error in DataIngestion initialization: {str(e)}")
            raise BankChurnException(f"Error during DataIngestion initialization: {str(e)}", sys) from e



    def export_data_into_artifact_data(self) -> DataFrame:
        try:
            logging.info("Exporting data from MySQL Database")
            hotel_booking_data = HotelBookingData()
            dataframe = hotel_booking_data.export_data_as_dataframe(dataset_name=self.dataset_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")


            artifact_raw_file_path = self.data_ingestion_config.raw_file_path
            dir_path = os.path.dirname(artifact_raw_file_path)
            os.makedirs(dir_path, exist_ok=True)


            logging.info(f"Saving exported data into artifact raw file path: {artifact_raw_file_path}")
            save_data(dataframe, artifact_raw_file_path)
        
            return dataframe
        except Exception as e:
            logging.error(f"Error in export_data_into_artifact_data: {str(e)}")
            raise BankChurnException(f"Error in export_data_into_artifact_data: {str(e)}",sys) from e



    def drop_insignificant_columns(self, dataframe: DataFrame) -> DataFrame:
        """
        Method Name :   drop_insignificant_columns
        Description :   This method drops insignificant columns from the dataframe.

        Output      :   DataFrame with insignificant columns removed.
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered drop_insignificant_columns method of DataIngestion class")

        try:
            # Retrieve insignificant columns from schema config
            insignificant_columns = self._schema_config.get("insignificant_columns", [])

            if insignificant_columns:
                logging.info(f"Removing insignificant columns: {insignificant_columns}")
                dataframe = dataframe.drop(columns=insignificant_columns, errors="ignore")


            logging.info("Exited drop_insignificant_columns method of DataIngestion class")
            return dataframe
        
        except Exception as e:
            logging.error(f"Error in drop_insignificant_columns: {str(e)}")
            raise BankChurnException(f"Error in drop_insignificant_columns: {str(e)}", sys) from e
        


    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline

        Output      :   Ingested data is saved as a CSV file.
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            dataframe = self.export_data_into_artifact_data()
            logging.info("Got the data from MySQL Database")


            dataframe = self.drop_insignificant_columns(dataframe)
            logging.info("Dropped insignificant columns from the dataframe")


            data_file_path = self.data_ingestion_config.data_file_path
            dir_path = os.path.dirname(data_file_path)
            os.makedirs(dir_path, exist_ok=True)


            logging.info(f"Saving ingested data into file path: {data_file_path}")
            save_data(dataframe, data_file_path)

            
            data_ingestion_artifact = DataIngestionArtifact(data_file_path=data_file_path)
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
        
        
            logging.info("Exited initiate_data_ingestion method of DataIngestionClass")
            return data_ingestion_artifact
        
        except Exception as e:
            logging.error(f"Error in initiate_data_ingestion: {str(e)}")
            raise BankChurnException(f"Error in initiate_data_ingestion: {str(e)}", sys) from e