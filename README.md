# CKD Predictor Web Application

## Overview
This project is a web application that predicts Chronic Kidney Disease (CKD) using machine learning techniques and the Flask web framework. It involves data handling, preprocessing, training a Support Vector Machine (SVM) model, and implementing a user-friendly interface for CKD prediction.

## Features
- **Data Handling & Preprocessing:** Processed medical data using Python libraries like NumPy and Pandas, performed data cleaning, and encoded categorical variables.
  
- **Machine Learning Model:** Trained an SVM classifier to predict CKD based on health indicators like serum creatinine, hemoglobin levels, etc., achieving high accuracy.
  
- **Web Development with Flask:** Implemented a user-friendly interface allowing users to input health parameters for CKD prediction and displaying disease likelihood.
  
- **Performance Evaluation:** Evaluated model performance using metrics like recall, precision, and F1-score.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/harshmahalle/CKD-Detection-SVM.git
   cd CKD-Predictor
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application locally:
   ```
   python app.py
   ```
   The application will be accessible at `http://localhost:5000`.

## Accessing the Demo

### Locally
To access the demo locally:
1. Follow the installation steps above.
2. Open your web browser and go to `http://localhost:5000`.

### Globally

#### PythonAnywhere
To host the application on PythonAnywhere:
1. Create a PythonAnywhere account and set up a Flask web application.
2. Upload your project files to PythonAnywhere.
3. Configure the web application to run `app.py`.
4. Access your hosted application through PythonAnywhere's provided URL.

#### Vercel
To deploy the application on Vercel:
1. Create a Vercel account and install the Vercel CLI.
2. Use the Vercel CLI to deploy your Flask application.
3. Vercel will provide you with a URL to access your deployed application.

#### Heroku
To deploy the application on Heroku:
1. Create a Heroku account and install the Heroku CLI.
2. Push your project to Heroku using Git.
3. Configure your Heroku app to run `app.py`.
4. Access your hosted application through Heroku's provided URL.

## Support
For any issues or questions, please contact [Harsh Mahalle](mailto:mahalleharsh9@gmail.com).
