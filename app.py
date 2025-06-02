from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and class names from pickle
model_path = 'iris_model.pkl'
with open(model_path, 'rb') as model_file:
    model, class_names = pickle.load(model_file)

# Ensure model has predict method
if not hasattr(model, 'predict'):
    raise AttributeError("Loaded model does not support prediction.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values
        sepal_length = float(request.form.get('sepal_length'))
        sepal_width = float(request.form.get('sepal_width'))
        petal_length = float(request.form.get('petal_length'))
        petal_width = float(request.form.get('petal_width'))

        # Prepare input array
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(features)[0]

        # Map prediction index to class name
        predicted_class = class_names[prediction]
        return render_template('index.html', prediction_text=f"Predicted Iris Species: {predicted_class}")

    except Exception as e:
        return render_template('index.html', error_message=f"Error: {str(e)}")

# Use gunicorn or Azure’s default server in production
if __name__ == '__main__':
    app.run()
