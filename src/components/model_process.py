import os
import sys
import pandas as pd
import numpy as np
from src.logger import logging
from sklearn.metrics.pairwise import cosine_similarity
from src.exception import custom_execption
import pickle


class model_process:
    try: 
        def get_similarities(self,song_data,raw_data,vec):
            vectors=pickle.load(open(vec,'rb'))
            logging.info("get similarities started")
            text1=vectors.transform(raw_data[raw_data['name']== song_data]['genres']).toarray()
            num_1=raw_data[raw_data['name']==song_data].select_dtypes(include=np.number).to_numpy()
            logging.info("vector process 1 completed")
            similar=[]
            logging.info("similarity started")
            for i,j in raw_data.iterrows():
                song_name=j['name']
                text2=vectors.transform(raw_data[raw_data['name']==song_name]['genres']).toarray()
                num_2=raw_data[raw_data['name']==song_name].select_dtypes(include=np.number).to_numpy()
                similarity1=cosine_similarity(text1,text2)[0][0]
                similarity2=cosine_similarity(num_1,num_2)[0][0]
                final_similar=similarity1+similarity2
                similar.append(final_similar)
            logging.info("similarity process ended")
            return similar
    except Exception as e:
        raise custom_execption(e,sys)
    try:
        def recommend_process1(self,song_name,data_,vector):
            logging.info("recommend process1 started")
            logging.info("pickle load!")
            logging.info("pickle loading process sucessful")
            if data_[data_['name']==song_name].shape[0] == 0:
                p=[]
            else:
                data_['similarity']=self.get_similarities(song_name,data_,vector)
                data_.sort_values(by=['similarity','popularity'],ascending=[False,False],inplace=True)
                p=data_[['name','artists']][2:7]
                logging.info(f"recommendations are {p}")
            return p
    except Exception as e:
        raise custom_execption(e,sys)
    