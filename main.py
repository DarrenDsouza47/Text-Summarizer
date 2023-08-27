from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
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


STAGE_NAME="Stage 02 data validation"

try:
    logger.info(f">>>>>stage {STAGE_NAME}<<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>stage {STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e