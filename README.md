# Disease Prediction System

A machine learning-based web application that predicts potential diseases from user-selected symptoms. Built with Python and Flask, the application uses an ensemble of machine learning classifiers to provide prediction results through an interactive web interface.

> **Medical Disclaimer:** This project is intended for educational and informational purposes only. Its predictions are not medical diagnoses and must not replace advice from a qualified healthcare professional.

## Overview

The Disease Prediction System demonstrates how machine learning can be integrated into a web application to classify diseases based on reported symptoms.

The system converts selected symptoms into a numerical feature vector and passes it to a trained ensemble model. The application then presents the prediction results through its web interface.

## Features

- Interactive symptom selection
- Symptom-based disease classification
- Ensemble machine learning using soft voting
- Random Forest, XGBoost, and LightGBM classifiers
- Prediction results with confidence scores
- Flask-based backend and prediction endpoints
- HTML, CSS, and JavaScript frontend
- Model evaluation reports and visualizations

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend | Flask, Flask-CORS |
| Frontend | HTML, CSS, JavaScript |
| Machine Learning | Scikit-learn, XGBoost, LightGBM |
| Data Processing | Pandas, NumPy |
| Model Storage | Pickle, gzip |
| Version Control | Git, GitHub |

## How It Works

1. **Symptom selection:** The user selects symptoms through the web interface.
2. **Feature preparation:** Selected symptoms are converted into the feature format expected by the trained model.
3. **Ensemble prediction:** Random Forest, XGBoost, and LightGBM contribute to the soft-voting classifier.
4. **Results:** The application displays the predicted disease information and associated prediction scores.

## Project Structure

```text
Diseases-Prediction-based-on-Symptoms/
├── Dataset/                     # Training datasets
├── static/
│   ├── index.html                # Web interface
│   ├── script.js                 # Frontend interactions
│   └── style.css                 # Styling
├── app.py                        # Flask application
├── train_combine.py              # Model training
├── symptoms_list.json            # Symptom names
├── diseases_list.json            # Disease labels
├── model_info.json               # Model metadata
├── classification_report.txt     # Evaluation report
├── confusion_matrix.png          # Evaluation visualization
├── feature_importance.png        # Feature importance visualization
├── requirements.txt              # Python dependencies
├── check_model_size.py            # Model inspection utility
├── compress_model.py              # Model compression utility
├── verify_compressed_model.py     # Compressed model verification
└── README.md
```

## Installation and Setup

### Prerequisites

- Python installed on your system
- Git
- Required datasets in the `Dataset/` directory

### 1. Clone the repository

```bash
git clone https://github.com/gaurangmishra1/Diseases-Prediction-based-on-Symptoms.git
cd Diseases-Prediction-based-on-Symptoms
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell activation is restricted, you can use Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Generate the model

The trained model files are not stored in this GitHub repository because of their size.

Ensure the required datasets are present in `Dataset/`, then run:

```bash
python train_combine.py
```

Model training may require substantial memory, storage, and processing time.

### 5. Run the application

After model training completes successfully, start Flask:

```bash
python app.py
```

Open the application in your browser:

**http://127.0.0.1:5000**

Keep the terminal running while using the application.

## Model Evaluation

The project includes evaluation artifacts such as:

- Classification report
- Confusion matrix
- Feature importance visualization

The model metadata is available in `model_info.json`. Evaluation metrics should be interpreted in the context of the dataset and evaluation procedure; they do not establish clinical reliability.

## Model Storage

The trained model is excluded from GitHub because of its large file size. The application supports loading the compressed model file when available and falls back to the uncompressed model file.

The helper scripts `compress_model.py` and `verify_compressed_model.py` support model compression and loading verification.

## Future Improvements

- Deploy the application with suitable compute resources
- Add automated tests for prediction endpoints
- Improve model evaluation and validation
- Enhance accessibility and usability
- Explore additional model comparison and explainability techniques

## Author

**Gaurang Mishra**

- GitHub: [@gaurangmishra1](https://github.com/gaurangmishra1)

## Disclaimer

This project is a machine learning demonstration for educational purposes. It is not intended to diagnose, treat, cure, or prevent any disease. Always consult a qualified healthcare professional for medical concerns.
