import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
data = pd.read_csv("U:\Heart disease\heart.csv")  # Adjust path as necessary

# Select features and target
X = data.drop('target', axis=1)
y = data['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open('Z:/heart_disease_model.sav', 'wb') as model_file:  # Adjust path as necessary
    pickle.dump(model, model_file)

print(f'Model trained with accuracy: {model.score(X_test, y_test)}')
