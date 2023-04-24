## trying to predict the flight fare based on 452000+ flight price records

 i have collected this dataset from below link
 url : https://www.kaggle.com/datasets/yashdharme36/airfare-ml-predicting-flight-fares


# usage

Over 450000 datas of flight records this machine learning algorithm can predict the flight price between certain indain cities
. users can input the features such as date, airline ,class, duration ,source and destinantion 

# Installation
To run this application on your local machine, follow these steps:

1. Clone this repository to your local machine using git clone https://github.com/your-username/flightpriceWEBAPP.git
2. Navigate to the project directory using cd flightpriceWEBAPP
3. Install the required packages using pip install -r requirements.txt
4. Start the Flask development server using python app.py
5. Open your web browser and go to http://localhost:5000


# Training of the model

after searching for a better algorithmsm , i have concluded that random forest regressor gives the best score. so this model have been trained on random forest regressor from scikit-learn

# data-preprocessing
 
 preprocessor object is also saved for the transformation of new dataframe
 we have used pickle library to save both model and preprocessor. 

 