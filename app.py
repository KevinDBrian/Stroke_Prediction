# imports
import pickle
import numpy as np
from flask import Flask, render_template, request

# load model
with open('model/model.pkl', 'rb') as model:
    model = pickle.load(model)

# declare Flask app
app = Flask(__name__)

# - - - - - main function - - - - -

if __name__ == '__main__':
    app.run(debug=True)


# default web page
@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        clf = joblib.load("clf.pkl")
        
        # Get values through input bars
        height = request.form.get("height")
        weight = request.form.get("weight")
        
        # Put inputs to dataframe
        X = pd.DataFrame([[height, weight]], columns = ["Height", "Weight"])
        
        # Get prediction
        prediction = clf.predict(X)[0]
        
    else:
        prediction = ""
        
    return render_template("website.html", output = prediction)

def predict():
    # rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_feautres = [np.array(int_features)]
    prediction = model.predict(final_feautres)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='CO2    Emission of the vehicle is :{}'.format(output))

