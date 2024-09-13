
from src.mlProject.entity.config_entity import *
from sklearn.metrics import accuracy_score
import pandas as pd 
import joblib
from src.mlProject.utils.common import save_json
import os
from pathlib import Path
from src.mlProject import logging

class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig) -> None:
        self.config=config
        
    def eval_metrics(self,actual,pred):
        acc_score=accuracy_score(actual,pred)
        
        return acc_score
    
    def save_predication(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)
        
        target_col='RiskLevel'
        
        X_test=test_data.drop(columns=target_col,axis=1)
        y_test=test_data[[target_col]]
        
        prediction=model.predict(X_test)
        
        acc_score=self.eval_metrics(y_test,prediction)
        logging.info(acc_score)
        
        score={'acc_score':acc_score}
        
        save_json(Path(self.config.metrics_file_name),data=score)