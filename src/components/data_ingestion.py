import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #Used to directly instantiate class variables without using __inin__() since there are only variables and no funcitons.
#This class will be used to keep track of where tp keep tran, test, raw data etc.
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts',"train.csv") #Save train data here after data ingestion is complete.
    test_data_path = os.path.join('artifacts', "test.csv") #Save test data here after data ingestion is complete.
    raw_data_path = os.path.join('artifacts', "data.csv") #Save raw data here after data ingestion is complete.


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")

        try:
            #Read the raw data from any bdata scource
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Dataset has been read successfully.')

            #Create the train,test and raw directories
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header= True)

            logging.info('Train test split initiated.')
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=45)

            #Convert train and test set to csv
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Train test split successful. Data Ingestion is complete.')

            #Return train and test data for Data Transformantion stage.
            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                    )

        except Exception as e:
            raise CustomException(e,sys)










