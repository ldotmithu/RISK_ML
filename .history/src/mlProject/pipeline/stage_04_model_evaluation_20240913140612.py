
from src.mlProject.config.configuration import *
from src.mlProject.components.model_evaluation import *

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config=ConfigManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.save_predication()