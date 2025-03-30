from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import config


app=Flask(__name__)

models_path=config.models_path
ridge_model=pickle.load(open(f'{models_path}/ridge.pkl','rb'))
scaler_model=pickle.load(open(f'{models_path}/scaler.pkl','rb'))
linear_model=pickle.load(open(f'{models_path}/linear.pkl','rb'))



## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    try:
        # ✅ 1. Receive input values from the form
        Temperature = float(request.form['Temperature'])
        RH = float(request.form['RH'])
        Ws = float(request.form['Ws'])
        Rain = float(request.form['Rain'])
        FFMC = float(request.form['FFMC'])
        DMC = float(request.form['DMC'])
        ISI = float(request.form['ISI'])
        Classes = float(request.form['Classes'])  # Ensure this is numeric
        Region = float(request.form['Region'])    # Ensure this is numeric

        # Convert input into a DataFrame (Fixes the feature name warning)
        feature_values = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        feature_names = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'Classes', 'Region']
        features_df = pd.DataFrame(feature_values, columns=feature_names)

        #new_data_scaled=scaler_model.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        #result=ridge_model.predict(new_data_scaled)
        #return render_template('home.html',result=result[0])

        # Scale the input data
        features_scaled = scaler_model.transform(features_df)

        #  Make the prediction
        prediction = ridge_model.predict(features_scaled)  # Extract single prediction

        return render_template('home.html', result=prediction[0])

    except Exception as e:
        return render_template('home.html', result=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)


