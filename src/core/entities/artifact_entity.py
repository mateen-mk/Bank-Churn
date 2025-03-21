from dataclasses import dataclass



# Data Ingestion Artifact
@dataclass
class DataIngestionArtifact:
    data_file_path: str


# Data Validation Artifact
@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    validation_report_file_path: str