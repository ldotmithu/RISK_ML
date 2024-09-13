from mlProject.pipeline.stage_01_data_ingestion import DataIngestionConfigTrainingPipeline
from src.mlProject.pipeline.stage_02_data_transfomation import DataTransfomationTrainingPipeline
from src.mlProject.pipeline.stage_03_model_train import ModelTrainPipeline
from mlProject import logging

stage_name='Data Ingestion'
try:
    data_ingestion=DataIngestionConfigTrainingPipeline()
    data_ingestion.main()
    logging.info('Data Ingestion Completed')
    
except Exception as e:
    logging.exception(e)
    raise e    

stage_name='Data Transfomation'
try:
    data_Transfomation=DataTransfomationTrainingPipeline()
    data_Transfomation.main()
    logging.info('Data Transfomation Completed')
    
except Exception as e:
    logging.exception(e)
    raise e 


stage_name='Model Train'
try:
    model_train=ModelTrainPipeline()
    model_train.main()
    logging.info('model_train Completed')
    
except Exception as e:
    logging.exception(e)
    raise e 