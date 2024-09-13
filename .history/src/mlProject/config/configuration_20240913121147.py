from mlProject.entity import  *
from mlProject import logging
from mlProject.utils.common import read_yaml,create_directories
from mlProject.constants import *

class ConfigurationManager:
    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        
    create_directories([self.config.artifacts_root])    