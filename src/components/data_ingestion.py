import os
import sys
from src.logger import logging
from src.exception import custom_execption
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.components.data_transformation import transform
from src.components.model_process import model_process
logging.info('data ingest started!')
@dataclass
class data_detail:
    data_path=os.path.join('Artifacts','data.csv')
    tracks_path=os.path.join('Artifacts','tracks.csv')
    logging.info('paths are created for data')
    
class data_ingest:
    def __init__(self):
        self.data_paths=data_detail()
        logging.info("data paths created !")
    
    
    def data_dividing(self):
        logging.info('enter the data ingestion part 2')        
        data=pd.read_csv(r"C:\Users\manoj\Desktop\music_recommendation\songs_data\top_10000_1960-now.csv")
        logging.info("data has read sucessfuly")
        tracks=pd.DataFrame({"name":data['Track Name'],
                             "artists":data['Artist Name(s)'],
                             "genres":data['Artist Genres'],
                             "release_year":data["Album Release Date"],
                             "duration":data["Track Duration (ms)"],
                             "popularity":data["Popularity"],
                             "Danceability":data["Danceability"],
                             "Energy":data["Energy"],
                             
                             "Key":data["Key"],
                             "Liveness":data["Liveness"],
                             "Valence":data["Valence"],
                             "Tempo":data["Tempo"],
                             "Time Signature":data["Time Signature"]})
        logging.info("dataframe had created sucessfuly")
        os.makedirs(os.path.dirname(self.data_paths.data_path),exist_ok=True)
        logging.info("directory has created")
        try:
            data.to_csv(self.data_paths.data_path,header=True,index=False)
            tracks.to_csv(self.data_paths.tracks_path,header=True,index=False) 
            logging.info("data ingest sucessfully")
            return(
                self.data_paths.data_path,
                self.data_paths.tracks_path
            ) 
        except Exception as e:
            raise custom_execption(e,sys)



    
    