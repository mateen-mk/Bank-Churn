import os

from from_root import from_root
from dataclasses import dataclass

from src.core.constants.common import *
from src.core.constants.directory import *
from src.core.constants.data import *
from src.core.constants.model import *


# Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    raw_data_dir = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, RAW_DATA_DIR)
    interim_data_dir = os.path.join(from_root(),ARTIFACTS_DIR, DATA_DIR, INTERIM_DATA_DIR)
    raw_file_path: str = os.path.join(raw_data_dir, DATA_INGESTION_RAW_FILE) 
    data_file_path: str = os.path.join(interim_data_dir, DATA_INGESTION_DATA_FILE)


# Data Validation Configuration
@dataclass
class DataValidationConfig:
    validation_report_dir = os.path.join(from_root(), ARTIFACTS_DIR, REPORTS_DIR, VALIDATION_REPORT_DIR)
    validation_report_file_path: str = os.path.join(validation_report_dir, DATA_VALIDATION_REPORT)