ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constants
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/19wWuQ6yeNrjMOrbJHwMtjk_zINGU2f1p/view?usp=sharing"


"""
Data validation related constants
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE: str = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "data.yaml"]


"""
Model trainer related constants
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16