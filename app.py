from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np 

#ml packages
from sklearn.feature_extraction import CountVectorization
from sklearn.externals import joblib

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    df = pd.read_csv('data/names_dataset.csv')


if __name__ == '__main__':
    app.run(debug=True) 

