from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME="Stage 01 data ingestion"

try:
    logger.info(f">>>>>stage {STAGE_NAME}<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>stage {STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e