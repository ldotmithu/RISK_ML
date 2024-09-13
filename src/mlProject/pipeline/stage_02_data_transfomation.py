from src.mlProject.config.configuration import *
from src.mlProject.components.data_transfomation import DataTransfomation

class DataTransfomationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigManager()
        data_tranfomation_config=config.get_data_transfomation_config()
        data_tranfomation=DataTransfomation(config=data_tranfomation_config)
        data_tranfomation.split()