import sys
import pandas as pd
from exception import CustomException
from utils import load_object
from logger import logging
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'random_forest_model.pkl')
            preprocessor_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'preprocessor.pkl')

            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            logging.info("loaded model and preprocessor")
            data_scaled=preprocessor.transform(features)
            logging.info("data transformation completed")
            prediction=model.predict(data_scaled)
            logging.info("model predicted inside predict pipeline")
            return prediction
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        Airline: str,
        Classes: str,
        Source: str,
        Departure: str,
        Total_stops: str,
        Arrival: str,
        Destination: str,
        Duration_in_hours: float,
        Days_left: int,
        Year: int,
        Month: int,
        Day: int,
        Day_of_week: int):

        self.Airline = Airline
        self.Classes = Classes
        self.Source = Source
        self.Departure = Departure
        self.Total_stops = Total_stops
        self.Arrival = Arrival
        self.Destination = Destination
        self.Duration_in_hours = Duration_in_hours
        self.Days_left = Days_left
        self.Year = Year
        self.Month = Month
        self.Day = Day
        self.Day_of_week =Day_of_week

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Airline": [self.Airline],
                "Classes": [self.Classes],
                "Source": [self.Source],
                "Departure": [self.Departure],
                "Total_stops": [self.Total_stops],
                "Arrival": [self.Arrival],
                "Destination": [self.Destination],
                "Duration_in_hours": [self.Duration_in_hours],
                "Days_left": [self.Days_left],
                "Year": [self.Year],
                "Month": [self.Month],
                "Day": [self.Day],
                "Day_of_week": [self.Day_of_week],
            }
            logging.info("dataframe created inside predict_pipeline.py")
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
