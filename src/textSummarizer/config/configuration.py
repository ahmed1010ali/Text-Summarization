from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig,
                                   DataValidationConfig,
                                   DataTransformationConfig,
                                   ModelTrainerConfig,
                                   ModelEvaluationConfig)



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
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            # Check for model_trainer key
            if "model_trainer" not in self.config:
                raise ValueError("Key 'model_trainer' not found in configuration.")

            config = self.config.model_trainer
            params = self.params.TrainingArguments

            # Ensure required directories exist
            create_directories([config.root_dir])

            # Construct ModelTrainerConfig object
            model_trainer_config = ModelTrainerConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                model_ckpt=config.model_ckpt,
                num_train_epochs=params.num_train_epochs,
                warmup_steps=params.warmup_steps,
                per_device_train_batch_size=params.per_device_train_batch_size,
                weight_decay=params.weight_decay,
                logging_steps=params.logging_steps,
                evaluation_strategy=params.evaluation_strategy,
                eval_steps=params.evaluation_strategy,
                save_steps=params.save_steps,
                gradient_accumulation_steps=params.gradient_accumulation_steps
            )

            return model_trainer_config

        except KeyError as e:
            raise ValueError(f"Missing required configuration key: {str(e)}")
        except AttributeError as e:
            raise ValueError(f"Invalid configuration structure: {str(e)}")
        

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name   
        )

        return model_evaluation_config
        


