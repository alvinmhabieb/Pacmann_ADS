import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_and_evaluate_model(data_path, prediction_features, targeted_feature, model_save_path):
    data = pd.read_csv(data_path)

    X = data[prediction_features]
    y = data[targeted_feature]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    model = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=5)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(predictions, y_test)
    report = classification_report(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)

    pickle.dump(model, open(model_save_path, 'wb'))

    return model, accuracy, report, cm

def load_model(file_path):
    return pickle.load(open(file_path, 'rb'))

def prepare_new_data(new_data):
    new_data = np.array(list(new_data.values())).reshape(1, -1)
    return StandardScaler().fit_transform(new_data)

if __name__ == "__main__":
    data_path = '/content/drive/MyDrive/Colab Notebooks/dataset/cancer_breast_data.csv'
    prediction_features = ['radius_mean', 'perimeter_mean', 'area_mean', 'symmetry_mean', 'compactness_mean', 'concave_points_mean']
    targeted_feature = 'diagnosis'
    model_save_path = 'model.pkl'

    # Train and evaluate the model
    model, accuracy, report, cm = train_and_evaluate_model(data_path, prediction_features, targeted_feature, model_save_path)

    # Load the model
    loaded_model = load_model(model_save_path)

    # Prepare new data for prediction
    new_data = {
        'radius_mean': 15.0,
        'perimeter_mean': 100.0,
        'area_mean': 700.0,
        'symmetry_mean': 0.2,
        'compactness_mean': 0.3,
        'concave_points_mean': 0.1
    }
    prepared_new_data = prepare_new_data(new_data)

    # Use the loaded model for prediction
    new_predictions = loaded_model.predict(prepared_new_data)
    print(new_predictions)