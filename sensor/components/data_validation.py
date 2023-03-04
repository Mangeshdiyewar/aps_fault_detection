from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
from typing import Optional
import os,sys 
import pandas as pd
from sensor.utils import utils
import numpy as np
from sensor.config import TARGET_COLUMN


class DataValidation:

    def __init__(self,
                 data_validation_config :config_entity.DataValidationConfig,
                 data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact =data_ingestion_artifact
            self.data_validation_error =dict()
        except Exception as e:
            raise SensorException(e,sys)

    def drop_missing_values_columns(self,df:pd.DataFrame, report_key_name:str)->Optional[pd.DataFrame]:
        """
        This function will drop column which contains missing value more than specified threshold
        df: Accepts a pandas dataframe
        threshold: Percentage criteria to drop a column
        =====================================================================================
        returns Pandas DataFrame if atleast a single column is available after missing columns drop else None
        """
        try:

            threshold = self.data_validation_config.missing_threshold
            null_report = df.isna().sum()/df.shape[0]
            #selecting column name which contains null
            logging.info(f"selecting column name which contains null above to {threshold}")
            drop_column_names= null_report[null_report>threshold].index

            logging.info(f"columns to drop:{list(drop_column_names)}")
            self.data_validation_error[report_key_name]=list(drop_column_names)
            df.drop(list(drop_column_names),axis=1,inplace =True)

            #return None no of columns left

            if len(df.columns)==0:
                return None
            return df

        except Exception as e :
            raise SensorException(e,sys)



