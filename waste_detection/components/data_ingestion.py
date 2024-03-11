import os
import sys
import zipfile
import gdown
from waste_detection.logger import logging
from waste_detection.exception import AppExeption
from waste_detection.entity.config_entity import DataIngestionConfig
from waste_detection.entity.artifacts_entity import DataIngestionArtifact
from pathlib import Path


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppExeption(e,sys) from e
        
    def download_data(self) -> str:
        """
        Fetch the data from the google drive 
        """

        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_file_path)

            logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")

            return zip_file_path
        
        except Exception as e:
            raise AppExeption(e, sys) from e
        
    def extract_zip_files(self, zip_file_path: str) -> str:
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip:
                zip.extractall(feature_store_path)  
            logging.info(f"Extracting zip file: {zip_file_path} into dir: {feature_store_path}")

            return feature_store_path
        
        except Exception as e:
            raise AppExeption(e,sys) from e
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the data ingestion mode")
        try:
            # zip_file_path = self.download_data()
            zip_file_path = "artifacts/data_ingestion/waste_detection.zip"
            feature_store_path = self.extract_zip_files(zip_file_path)

            data_ingestion_artifacts = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )
            
            logging.info("Exited the data ingestion mode")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifacts}")

            return data_ingestion_artifacts
        
        except Exception as e:
            raise AppExeption(e,sys) from e
        
        