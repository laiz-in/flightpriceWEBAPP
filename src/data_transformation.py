import sys
from dataclasses import dataclass
import os
import pickle

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformation:
    
    def get_data_transformer(self,Journey_day,Journey_month,Dep_hour, Dep_min ,Arrival_hour,Arrival_min,Duration_hours,Duration_mins,Total_Stops,Airline,Source,Destination):
        try:

            data = {'Journey_day': Journey_day, 'Journey_month': Journey_month, 'Dep_hour': Dep_hour,'Dep_min':Dep_min,
                    'Arrival_hour':Arrival_hour,'Arrival_min':Arrival_min,'Duration_hours':Duration_hours,'Duration_mins':Duration_mins,'Total_Stops':Total_Stops,'Airline':Airline,
                    'Source':Source,'Destination':Destination}
           
            df = pd.DataFrame(data,index=[0])
            if(Airline=='Jet Airways'):
                Jet_Airways = 1
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 

            elif (Airline=='IndiGo'):
                Jet_Airways = 0
                IndiGo = 1
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 

            elif (Airline=='Air India'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 1
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
                
            elif (Airline=='Multiple carriers'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 1
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
            
            elif (Airline=='SpiceJet'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 1
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
            
            elif (Airline=='Vistara'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 1
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (Airline=='GoAir'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 1
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (Airline=='Multiple carriers Premium economy'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 1
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (Airline=='Jet Airways Business'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 1
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (Airline=='Vistara Premium economy'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 1
                Trujet = 0
                
            elif (Airline=='Trujet'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 1

            else:
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0
      
            if (Source == 'Delhi'):
                s_Delhi = 1
                s_Kolkata = 0
                s_Mumbai = 0
                s_Chennai = 0

            elif (Source == 'Kolkata'):
                s_Delhi = 0
                s_Kolkata = 1
                s_Mumbai = 0
                s_Chennai = 0

            elif (Source == 'Mumbai'):
                s_Delhi = 0
                s_Kolkata = 0
                s_Mumbai = 1
                s_Chennai = 0

            elif (Source == 'Chennai'):
                s_Delhi = 0
                s_Kolkata = 0
                s_Mumbai = 0
                s_Chennai = 1

            else:
                s_Delhi = 0
                s_Kolkata = 0
                s_Mumbai = 0
                s_Chennai = 0

            if (Source == 'Cochin'):
                d_Cochin = 1
                d_Delhi = 0
                d_New_Delhi = 0
                d_Hyderabad = 0
                d_Kolkata = 0
            
            elif (Source == 'Delhi'):
                d_Cochin = 0
                d_Delhi = 1
                d_New_Delhi = 0
                d_Hyderabad = 0
                d_Kolkata = 0

            elif (Source == 'New_Delhi'):
                d_Cochin = 0
                d_Delhi = 0
                d_New_Delhi = 1
                d_Hyderabad = 0
                d_Kolkata = 0

            elif (Source == 'Hyderabad'):
                d_Cochin = 0
                d_Delhi = 0
                d_New_Delhi = 0
                d_Hyderabad = 1
                d_Kolkata = 0

            elif (Source == 'Kolkata'):
                d_Cochin = 0
                d_Delhi = 0
                d_New_Delhi = 0
                d_Hyderabad = 0
                d_Kolkata = 1

            else:
                d_Cochin = 0
                d_Delhi = 0
                d_New_Delhi = 0
                d_Hyderabad = 0
                d_Kolkata = 0


           
            model = pickle.load(open("ipynb_files/flight_fare.pkl", "rb"))
            logging.info("model loaded for prediction")
            prediction=model.predict([[
                        Total_Stops,
                        Journey_day,
                        Journey_month,
                        Dep_hour,
                        Dep_min,
                        Arrival_hour,
                        Arrival_min,
                        Duration_hours,
                        Duration_mins,
                        Air_India,
                        GoAir,
                        IndiGo,
                        Jet_Airways,
                        Jet_Airways_Business,
                        Multiple_carriers,
                        Multiple_carriers_Premium_economy,
                        SpiceJet,
                        Trujet,
                        Vistara,
                        Vistara_Premium_economy,
                        s_Chennai,
                        s_Delhi,
                        s_Kolkata,
                        s_Mumbai,
                        d_Cochin,
                        d_Delhi,
                        d_Hyderabad,
                        d_Kolkata,
                        d_New_Delhi
                        ]])
            logging.info("prediction completed")
            return prediction
        except Exception as e:
           raise CustomException(e,sys) 

     




         





