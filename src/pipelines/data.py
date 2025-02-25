# pipeline for src/data/ folder scripts

import sys

from src.core.logger import logging
from src.core.exception import BankChurnException

from src.core.entities.config_entity import DataIngestionConfig
from src.core.entities.artifact_entity import DataIngestionArtifact

from src.data.ingestion import DataIngestion



# Constructing a DataPipeline
class DataPipeline:
    """
    class name: DataPipeline
    Description: this class is used to create a pipeline for data scripts (src/data/<scripts>).
    """

    def __init__(self):

        logging.info("* "*50)
        logging.info("- - - - - Started DataPipeline - - - - -")
        logging.info("* "*50)
        
        self.data_ingestion_config = DataIngestionConfig()
        # self.data_validation_config = DataValidationConfig()
        # self.data_preprocessing_config = DataPreprocessingConfig()
        # self.data_split_config = DataSplitConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of DataPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("_"*100)
            logging.info("")
            logging.info("! ! ! Entered start_data_ingestion method of DataPipeline Class:")
            
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("- "*50)
            logging.info("- - - Data Ingested Successfully! - - -")

            logging.info("")
            logging.info("! ! ! Exited the start_data_ingestion method of DataPipeline class:")
            logging.info("_"*100)

            return data_ingestion_artifact
        
        except Exception as e:
            logging.error(f"Error in start_data_ingestion: {str(e)}")
            raise BankChurnException(f"Error in start_data_ingestion: {str(e)}",sys) from e
     