from mlProject.entity.config_entity import *
from mlProject.config.configuration import *
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd 



class ModelTrain:
    def __init__(self,config: ModelTrainConfig) -> None:
        self.config=config
        
    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
        
        X_train=train_data.drop(columns=)
        
        
    