
from src.mlProject.entity.config_entity import *
from sklearn.metrics import accuracy_score
import pandas as pd 
import joblib,os,json

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
        
        
            