import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names  # Get the class names

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocess the data (scale features)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Support Vector Machine classifier
model = SVC(kernel='linear', C=1.0, probability=True)
model.fit(X_train_scaled, y_train)

# Evaluate the model
accuracy = model.score(X_test_scaled, y_test)
print(f"Accuracy: {accuracy:.2f}")

# Save the model to a pickle file
model_path = 'iris_model.pkl'
with open(model_path, 'wb') as model_file:
    pickle.dump((model, class_names), model_file)

print(f"Model saved to {model_path}")

# Predict and print the class name for a sample
sample_features = [[5.1, 3.5, 1.4, 0.2]]  # Example sample features
sample_features_scaled = scaler.transform(sample_features)
predicted_class = model.predict(sample_features_scaled)[0]
predicted_class_name = class_names[predicted_class]
print(f"Prediction: The predicted iris species is: {predicted_class_name}")
