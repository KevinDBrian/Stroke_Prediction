# imports
import pickle
import numpy as np
from flask import Flask, render_template, request

# load model
with open('model/model.pkl', 'rb') as model:
    model = pickle.load(model)

# default web page
@app.route('/')
def home():
    return render_template('index.html')

def predict():
    # rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_feautres = [np.array(int_features)]
    prediction = model.predict(final_feautres)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='CO2    Emission of the vehicle is :{}'.format(output))