from mlProject.entity.config_entity import DataTransfomationConfig
from sklearn.preprocessing import StandardScaler

class DataTransfomation:
    def __init__(self,config:DataTransfomationConfig):
        self.config=config
        
    def preprocess(self):
            
    