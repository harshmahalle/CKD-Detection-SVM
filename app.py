# Importing required libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.svm import SVC
from flask import Flask, request, render_template
from sklearn.metrics import recall_score, precision_score, f1_score

app = Flask(__name__)

# Loading the pre-trained model
svc_model = SVC(C=0.1, kernel='linear', gamma=1, probability=True)
svc_model.fit(X_train, y_train)

# Loading the MinMaxScaler
x_scaler = MinMaxScaler()
x_scaler.fit(X)

# Function to preprocess input features and make predictions
def predict_ckd(features):
    x = np.array(features).reshape(1, -1)
    x = x_scaler.transform(x)
    y_pred = svc_model.predict(x)
    proba = svc_model.predict_proba(x)
    return y_pred[0], proba.max()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for predicting CKD
@app.route('/predict', methods=['POST'])
def predict():
    features = request.form.to_dict()
    for feature in features:
        features[feature] = float(features[feature])
    pred, proba = predict_ckd(list(features.values()))
    if pred == 0:
        return render_template('index.html', prediction_text='The patient has CKD with probability {:.2f}%'.format(proba*100))
    else:
        return render_template('index.html', prediction_text='The patient does not have CKD with probability {:.2f}%'.format(proba*100))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)