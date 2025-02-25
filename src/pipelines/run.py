import sys

from src.core.logger import logging
from src.core.exception import BankChurnException

from src.pipelines.data import DataPipeline



def run() -> None:
    """
    This method of run.py script is responsible for running the entire pipeline
    """
    try:
        data_pipeline = DataPipeline()
        # model_pipeline = ModelPipeline()
        logging.info("_"*100)
        logging.info("")
        logging.info("$ Entered run method of run.py script:")
        
        # start the data pipeline
        data_ingestion_artifact = data_pipeline.start_data_ingestion()
        # data_validation_artifact = data_pipeline.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        # data_preprocessing_artifact = data_pipeline.start_data_preprocessing(data_ingestion_artifact=data_ingestion_artifact, 
        #                                                                      data_validation_artifact=data_validation_artifact)
        # data_split_artifact = data_pipeline.start_data_split(data_preprocessing_artifact=data_preprocessing_artifact)
        
        # # start the model pipeline
        # model_trainer_artifact = model_pipeline.start_model_trainer(data_preprocessing_artifact=data_preprocessing_artifact, 
        #                                                             data_split_artifact=data_split_artifact)
        # model_evaluation_artifact = model_pipeline.start_model_evaluation(data_split_artifact=data_split_artifact,
        #                                                                   model_trainer_artifact=model_trainer_artifact)
        # model_validation_artifact = model_pipeline.start_model_validation(model_evaluation_artifact=model_evaluation_artifact)
        
        logging.info("")
        logging.info("$ Exited run method of run.py script:")
        logging.info("_"*100)
    
    except Exception as e:
        logging.error(f"Error in run method: {str(e)}")
        raise BankChurnException(f"Error in run() method: {str(e)}",sys) from e