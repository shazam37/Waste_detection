import sys, os
from waste_detection.logger import logging
from waste_detection.exception import AppExeption
from waste_detection.components.data_ingestion import DataIngestion
from waste_detection.components.data_validation import DataValidation
from waste_detection.entity.config_entity import DataIngestionConfig, DataValidationConfig
from waste_detection.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(
                "Entered the start data ingestion piepline"
            )
            logging.info("Getting the data from the URL")

            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info('Got the data from the url')
            logging.info("Exited the start data ingestion pipeline")
            

            return data_ingestion_artifact
        
        except Exception as e:
            raise AppExeption(e,sys) from e
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        logging.info("Entered the start data validation pipeline")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")
            logging.info("Exited the start data validation pipeline")

            return data_validation_artifact
        
        except Exception as e:
            raise AppExeption(e,sys) from e
    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
            )
        except Exception as e:
            raise AppExeption(e,sys) from e