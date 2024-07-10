from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained models
diabetes_model = pickle.load(open("U:\Heart disease\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("U:\Heart disease\heart_disease_model.sav", 'rb'))
liver_model = pickle.load(open("U:\Heart disease\model_lr_liver.sav", 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from form input and convert to integers
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    # Perform prediction using the heart disease model as an example
    prediction = heart_disease_model.predict(final_features)
    
    # Determine the output message based on prediction
    output = 'No Heart Disease' if prediction[0] == 0 else 'Heart Disease Detected'
    
    return render_template('index.html', prediction_text=f'Prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)
