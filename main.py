from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
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

STAGE_NAME="Stage 03 data transformation"

try:
    logger.info(f">>>>>stage {STAGE_NAME}<<<<<<")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>stage {STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e