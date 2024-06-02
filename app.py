from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and class names
model_path = 'iris_model.pkl'  # Ensure this path is correct
with open(model_path, 'rb') as model_file:
    model, class_names = pickle.load(model_file)

# Check if the loaded model has a predict method
if not hasattr(model, 'predict'):
    raise AttributeError("The loaded model does not have a 'predict' method.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        predicted_class_index = model.predict(features)[0]
        predicted_class_name = class_names[predicted_class_index]
        prediction_text = f'The predicted iris species is: {predicted_class_name}'

        return render_template('index.html', prediction_text=prediction_text)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
