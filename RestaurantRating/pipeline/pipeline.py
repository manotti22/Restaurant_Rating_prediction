from collections import namedtuple
from datetime import datetime
import uuid
from RestaurantRating.config.configuration import Configuration
from RestaurantRating.logger import logging, get_log_file_name
from RestaurantRating.exception import RestaurantRatingException
from threading import Thread
from typing import List

from multiprocessing import Process
from RestaurantRating.entity.artifact_entity import DataIngestionArtifact
from RestaurantRating.entity.config_entity import DataIngestionConfig
from RestaurantRating.component.data_ingestion import DataIngestion

import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd



class Pipeline(Thread):

    def __init__(self,config : Configuration=Configuration()) ->None:
        try:
            self.config= config 
        except Exception as e:
            raise RestaurantRatingException(e,sys) from e


    
   

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise RestaurantRatingException(e, sys) from e
    
    def run_pipeline(self):
        try:
           data_ingestion_artifact = self.start_data_ingestion()
           
        except Exception as e:
            raise RestaurantRatingException(e, sys) from e




