import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model = pickle.load(open('titanic.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp1 = float(request.args.get('exp1'))
    exp2 = float(request.args.get('exp2'))
    exp3 = float(request.args.get('exp3'))
    exp4 = float(request.args.get('exp4'))
    exp5 = float(request.args.get('exp5'))
    exp6 = float(request.args.get('exp6'))
    prediction = model.predict([[exp1,exp2,exp3,exp4,exp5,exp6]])
    print("Survived", prediction)
    if prediction==[1]:
        prediction="Passenger Survived"
    else:
        prediction="Passenger did not Survived"
    print(prediction)
    return prediction

if __name__ == "__main__":
    app.run(debug=True)