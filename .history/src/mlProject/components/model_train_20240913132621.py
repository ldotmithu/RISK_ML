from mlProject.entity.config_entity import *
from mlProject.config.configuration import *
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer


class ModelTrain:
    def __init__(self,config: ModelTrainConfig) -> None:
        self.config=config
        
    def preprocess(self):
        
        
    