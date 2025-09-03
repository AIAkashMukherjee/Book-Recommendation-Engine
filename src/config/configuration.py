import os
import sys
from src.logger.log import logging
from src.utils.util import read_yaml_file
from src.exception.exception_handler import CustomException
from src.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelRecommendationConfig
from src.constant import *


        
class ConfigManager:
    def __init__(self,config_file=CONFIG_FILE_PATH,
                 ):
        try:
            self.configs_info=read_yaml_file(config_file)

        except Exception as e:
            raise CustomException(e,sys)    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.configs_info['data_ingestion_config']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
            dataset_dir = data_ingestion_config['dataset_dir']

            ingested_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_dir'])
            raw_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['raw_data_dir'])

            response = DataIngestionConfig(
                dataset_download_url = data_ingestion_config['dataset_download_url'],
                raw_data_dir = raw_data_dir,
                ingested_dir = ingested_data_dir
            )

            logging.info(f"Data Ingestion Config: {response}")
            return response

        except Exception as e:
            raise CustomException(e, sys) 
