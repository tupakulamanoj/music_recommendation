import os
import sys 
from src.logger import logging
from src.exception import custom_execption
import pandas as pd
from dataclasses import dataclass
from sklearn.feature_extraction.text import CountVectorizer
import pickle
@dataclass
class data_transform:
    
    data_transform_path=os.path.join("Artifacts",'vectorization.pkl')
    logging.info(" vectorization paths are created")
class transform:
    def __init__(self):
        self.data_trans=data_transform()
    def transformation(self,data_path,track_path):
        try:
            logging.info("entered data transformation")
            track=pd.read_csv(track_path)
            logging.info("data read sucessfully for transformation!")
            track.drop_duplicates(subset=['name'],keep="first",inplace=True)
            logging.info("dropped duplicates")
            track.dropna(inplace=True)
            logging.info("data transformed sucess")
            c=CountVectorizer()
            c.fit_transform(track['genres'])
            logging.info("vectorization is sucessfully created")
            path=self.data_trans.data_transform_path
            pickle.dump(c,open(path,'wb'))
            logging.info("pickle file is created")
            data=pd.read_csv(data_path)
            return (
                track,
                data,
                path    
            )    
        
        
        except Exception as e:
            custom_execption(e,sys)