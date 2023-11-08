# main.py or any other module from which you want to import logger

from Cnn_Classifier import logger  # assuming that Cnn_Classifier is a Python package in the PYTHONPATH

from Cnn_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e