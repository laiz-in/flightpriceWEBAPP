# Predicting the flight fare based on 452000+ flight price records

I have collected this dataset from below link
https://www.kaggle.com/datasets/yashdharme36/airfare-ml-predicting-flight-fares


# Usage

Over 450000 datas of flight records this, machine learning algorithm can predict the flight price between certain indain cities
. users can input the features such as date, airline ,class, duration ,source and destinantion and get the fare predicited

# Installation
To run this application on your local machine, follow these steps:

1. Clone this repository to your local machine using git clone https://github.com/your-username/flightpriceWEBAPP.git
2. Navigate to the project directory using cd flightpriceWEBAPP
3. Install the required packages using pip install -r requirements.txt
4. Start the Flask development server using python app.py
5. Open your web browser and go to http://localhost:5000


# Training of the model

After researching for a better algorithm , i have concluded that random forest regressor gives the best score. so this model have been trained on random forest regressor from scikit-learn . and training tookplace for a few hours in my below specification with normal CPU

 - 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz   2.42 GHz
 - 16GB ram
 - nvidia 2GB dedicated graphics

# Data-preprocessing
 
 data-preprocessing meant to be terminating unwanted datas , null values
 extracting needful informations from existing columns and clean up the entire dataset

 all the steps are given in the jupyter notebook 
 
 preprocessor object is also saved for the transformation of new dataframe.
 we have used pickle library to save both model and preprocessor.
 

 