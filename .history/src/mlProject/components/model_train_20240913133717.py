from mlProject.entity.config_entity import *
from mlProject.config.configuration import *
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier


class ModelTrain:
    def __init__(self,config: ModelTrainConfig) -> None:
        self.config=config
        
    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
        train_data['RiskLevel']=train_data['RiskLevel'].map({'high risk':2,'mid risk':1,'low risk':0})
        test_data['RiskLevel']=test_data['RiskLevel'].map({'high risk':2,'mid risk':1,'low risk':0})
        
        target_col='RiskLevel'
        
        
        X_train=train_data.drop(columns=target_col,axis=1)
        X_test=test_data.drop(columns=target_col,axis=1)
        y_train=train_data[[target_col]]
        y_test=test_data[[target_col]]
        
        tree=DecisionTreeClassifier()
        tree.fit(X_train,y_train)
        
        
        
        
        
    