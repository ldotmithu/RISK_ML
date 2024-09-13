from src.mlProject.config.configuration import *
from mlProject.components.model_train import ModelTrain


class ModelTrainPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config=ConfigManager()
        model_training_config=config.get_model_training()
        