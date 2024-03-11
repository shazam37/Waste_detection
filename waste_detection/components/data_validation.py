import os
import sys
import shutil
from waste_detection.logger import logging
from waste_detection.exception import AppExeption
from waste_detection.entity.config_entity import DataValidationConfig
from waste_detection.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact

class DataValidation:
    def __init__(
            self,
            data_ingestion_artifact: DataIngestionArtifact,
            data_validation_config: DataValidationConfig 
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise AppExeption(e,sys) from e
        
    def validate_all_files_exists(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

            for file in all_files:
                if (file not in self.data_validation_config.required_file_list) or (os.path.getsize(self.data_validation_config.required_file_list) == 0):
                    validation_status=False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status=True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status:{validation_status}")

            return validation_status
        
        except Exception as e:
            raise AppExeption(e,sys) from e
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Entered the data validation mode")
        try:
            status = self.validate_all_files_exists()
            data_validation_artifact = DataValidationArtifact(validation_status=status)

            logging.info("Exited the data validation mode")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact
        
        except Exception as e:
            raise AppExeption(e,sys) from e