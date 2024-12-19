from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        self.config.artifacts_root = Path(self.config.artifacts_root)  # Explicit conversion
        create_directories([self.config.artifacts_root])

    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # Convert all paths to Path objects
        root_dir = Path(config.root_dir)
        local_data_file = Path(config.local_data_file)
        unzip_dir = Path(config.unzip_dir)

        # Create necessary directories
        create_directories([root_dir])

        return DataIngestionConfig(
            root_dir=root_dir,
            source_URL=config.source_URL,
            local_data_file=local_data_file,
            unzip_dir=unzip_dir,
        )