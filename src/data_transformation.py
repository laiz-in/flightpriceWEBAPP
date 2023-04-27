import sys
from dataclasses import dataclass
import os
import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from exception import CustomException
from logger import logging
from utils import save_object

@dataclass
class DataTransformationConfig:
    preprocess_obj_filepath = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        try:
            # define the categorical and numerical features
            categorical_features = ['Airline', 'Source', 'Departure', 'Classes','Total_stops', 'Arrival', 'Destination']
            numerical_features = ['Duration_in_hours', 'Days_left', 'Year', 'Month', 'Day', 'Day_of_week']
            
            # create the transformer for categorical features
            cat_transformer = Pipeline(steps=[
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])
            # create the column transformer
            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat', cat_transformer, categorical_features)    ])
            logging.info("preprocessor is created")
            return preprocessor
        except Exception as e:
           raise CustomException(e,sys) 
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df= pd.read_csv(train_path)
            test_df= pd.read_csv(test_path)
            logging.info("reading training and test data completed")
            logging.info("obtaining preprocessing object")
            preprocessor_obj= self.get_data_transformer_object()
            target_column_name= "Fare"

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
             
          
            logging.info("Applying preprocessing object on training dataframe and testing dataframe")

            
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)


            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocess_obj_filepath,
                obj=preprocessor_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocess_obj_filepath
            )
            
        except Exception as e:
            raise CustomException(e,sys)






         





