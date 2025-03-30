from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge


app=Flask(__name__)

ridge_model=pickle.load(open('models/ridge.pkl','rb'))
scaler_model=pickle.load(open('models/scaler.pkl','rb'))
linear_model=pickle.load(open('models/linear.pkl','rb'))



@app.route('/')
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")
