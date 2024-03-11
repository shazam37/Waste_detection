import sys, os
from waste_detection.logger import logging
from waste_detection.exception import AppExeption
from waste_detection.components.data_ingestion import DataIngestion
from waste_detection.entity.config_entity import DataIngestionConfig
from waste_detection.entity.artifacts_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

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
        
    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise AppExeption(e,sys) from e