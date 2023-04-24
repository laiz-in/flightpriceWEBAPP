import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats 
from scipy.stats import chi2_contingency
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import GradientBoostingRegressor
import joblib

#loading the dataset
df=pd.read_csv("dataset\Cleaned_dataset.csv")

#changing one column name from class to classes
df.rename(columns={'Class': 'Classes'}, inplace=True)

======================================================================================= TRNAFORM ARRIVAL AND DEP==================
# Create a function to transform Departure and Arrival columns
def transform_time(time):
    if time.endswith('AM'):
        if int(time.split(':')[0]) < 6:
            return 'Before 6 AM'
        else:
            return '6 AM - 12 PM'
    elif time.endswith('PM'):
        if int(time.split(':')[0]) >= 6:
            return 'After 6 PM'
        else:
            return '12 PM - 6 PM'

# # Update the 'Departure' and 'Arrival' columns in the new_data dataframe
# new_data['Departure'] = new_data['Departure'].apply(lambda x: transform_time(x.split('T')[1]))
# new_data['Arrival'] = new_data['Arrival'].apply(lambda x: transform_time(x.split('T')[1]))

# ======================================================================================================================

 #DROPPING THE FLIGHT_CODE COLUMN BECAUSE WE DONT REALLY NEED IT
# df.drop('Flight_code', axis=1, inplace=True)

# Load the pipeline object
# pipeline = joblib.load('pipeline.joblib')

# # Prepare new data as a pandas dataframe
# new_data = pd.DataFrame({
#     'Airline': ['Vistara'],
#     'Classes': ['Business'],
#     'Source': ['Ahmedabad'],
#     'Departure': ['6 AM - 12 PM'],
#     'Total_stops': ['1-stop'],
#     'Arrival': ['After 6 PM'],
#     'Destination': ['Chennai'],
#     'Duration_in_hours': [13.0833],
#     'Days_left': [50],
#     'Year': [2023],
#     'Month': [3],
#     'Day': [6],
#     'Day_of_week': [0]
# })


# # Predict using the pipeline
# y_pred = pipeline.predict(new_data)
# print(y_pred)
