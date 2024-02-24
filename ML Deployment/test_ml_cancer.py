# test_ml_cancer.py
import ml_cancer
# Sekarang Anda dapat menggunakan fungsi dan kelas dari modul ml_cancer seperti yang Anda butuhkan
from ml_cancer import train_and_evaluate_model, load_model, prepare_new_data
import numpy as np

def test_train_and_evaluate_model():
    # Tentukan data uji dan parameter
    data_path = 'C:\\Users\\Sharing-Vision\\Downloads\\cancer_breast_data.csv'
    prediction_features = ['radius_mean', 'perimeter_mean', 'area_mean', 'symmetry_mean', 'compactness_mean', 'concave points_mean']
    targeted_feature = 'diagnosis'
    model_save_path = 'test_model.pkl'

    # Latih dan evaluasi model
    model, accuracy, report, cm = train_and_evaluate_model(data_path, prediction_features, targeted_feature, model_save_path)

    # Periksa apakah model dilatih (opsional)
    assert model is not None

    # Periksa apakah akurasi adalah nilai yang valid (opsional)
    assert isinstance(accuracy, float)

    # Bersihkan setelah uji (opsional)
    # Anda mungkin ingin menghapus file model setelah pengujian

def test_load_model():
    # Tentukan data uji dan parameter
    model_file_path = 'test_model.pkl'

    # Muat model
    loaded_model = load_model(model_file_path)

    # Periksa apakah loaded_model adalah objek model yang valid (opsional)
    assert loaded_model is not None

def test_prepare_new_data():
    # Tentukan data uji
    new_data = {
        'radius_mean': 15.0,
        'perimeter_mean': 100.0,
        'area_mean': 700.0,
        'symmetry_mean': 0.2,
        'compactness_mean': 0.3,
        'concave points_mean': 0.1
    }

    # Siapkan data baru untuk prediksi
    prepared_new_data = prepare_new_data(new_data)

    # Periksa apakah prepared_new_data adalah array yang valid (opsional)
    assert isinstance(prepared_new_data, np.ndarray)
