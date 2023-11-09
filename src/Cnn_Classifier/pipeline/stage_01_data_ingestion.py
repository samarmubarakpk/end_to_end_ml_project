from Cnn_Classifier.config.configuration import ConfigurationManager
from Cnn_Classifier.components.data_ingestion import DataIngestion
from Cnn_Classifier import logger
from Cnn_Classifier.constant import *


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def  main(self):
        config = ConfigurationManager(CONFIG_FILE_PATH,PARAMS_FILE_PATH)
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e