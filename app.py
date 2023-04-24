from flask import Flask, request, render_template
from flask_cors import cross_origin
from src import data_ingestion
from src.data_transformation import DataTransformation
import pickle
import pandas as pd
from src.logger import logging
from src.exception import CustomException

app = Flask(__name__)
model = pickle.load(open("ipynb_files/flight_fare.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        Duration_hours = abs(Arrival_hour - Dep_hour)
        Duration_mins = abs(Arrival_min - Dep_min)
        Total_Stops = int(request.form["stops"])
        Airline=request.form['Airline']
        Source = request.form["Source"]
        Destination = request.form["Destination"]
        obj= DataTransformation()
        prediction=obj.get_data_transformer(Journey_day,Journey_month,Dep_hour, Dep_min ,Arrival_hour,Arrival_min,Duration_hours,Duration_mins,Total_Stops,Airline,Source,Destination)
        output=round(prediction[0],2)


        return render_template('home.html',prediction_text="₹ {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)