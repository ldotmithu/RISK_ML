
from mlProject.entity.config_entity import *
import zipfile,os
import urllib.request
from mlProject import logging


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            urllib.request.urlretrieve(self.config.URL,self.config.local_data_path)
            logging.info('file downloaded')
        else:
            logging.info('file already exists')    
            
    def extract_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_path,'r') as f:
            f.extractall(unzip_path)
            logging.info('file Extract successfull')        