import os
from pathlib import Path

list_of_files = [
    "src/configs/__init__.py",
    
    "src/data/__init__.py",
    "src/data/ingestion.py",
    "src/data/validation.py",
    "src/data/preprocessing.py",
    "src/data/split.py",

    "src/model/__init__.py",
    "src/model/trainer.py",
    "src/model/evaluation.py",
    "src/model/validation.py",
    "src/model/predictor.py",

    "src/pipelines/__init__.py",
    "src/pipelines/data.py",
    "src/pipelines/model.py",
    "src/mlops/__init__.py",

    "src/core/constants/__init__.py",
    "src/core/entities/__init__.py",
    "src/core/entities/artifact_entity.py",
    "src/core/entities/config_entity.py",
    "src/core/utils/__init__.py",
    "src/core/utils/helpers.py",
    "src/core/logger/__init__.py",
    "src/core/exception/__init__.py",
    
    "notebooks/trails.ipynb",
    "notebooks/figures",

    "settings/schema.yaml",
    "settings/model.yaml",
    
    "docs/api.md",
    "docs/setup.md",
    "docs/workflow.md",
    # "docs/architecture.md",
    
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "tests/e2e/__init__.py",
    
    # "deployment/api/__init__.py",
    # "deployment/docker",
    # "deployment/cloud/__init__.py",
        
    "logs/",

    ".env",
    ".gitignore",
    "app.py",
    "main.py",
    "Makefile",
    "README.md",
    "requirements.txt",
    "setup.py"
]

# Create directories and files
for filepath in list_of_files:
    if filepath.endswith("/"):  # Check if it's a directory
        os.makedirs(filepath, exist_ok=True)
        print(f'Created Folder: {filepath}')
    else:  # It's a file
        filepath = Path(filepath)
        filedir = filepath.parent
        if filedir:  # Ensure parent directory exists
            os.makedirs(filedir, exist_ok=True)
            print(f'Created File: {filepath}')
        if not filepath.exists():  # Create the file if it doesn't exist
            filepath.touch()
            print(f'Created/Touched File: {filepath}')