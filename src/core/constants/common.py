# src/constants/common_constant.py is used to store common constant values 

import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from.env file

# Common constants
TARGET_COLUMN: str = 'is_canceled'
SCHEMA_FILE_PATH = os.path.join("settings", "schema.yaml")


# MySQL constants
MYSQL_ENGINE_URL = os.getenv('MYSQL_ENGINE_URL')
DATABASE_NAME: str = 'projects_db'
DATASET_NAME: str = 'bank_churn'