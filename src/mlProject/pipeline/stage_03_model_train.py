from src.mlProject.config.configuration import *
from src.mlProject.components.model_train import ModelTrain


class ModelTrainPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config=ConfigManager()
        model_training_config=config.get_model_training()
        model_train=ModelTrain(config=model_training_config)
        model_train.train()