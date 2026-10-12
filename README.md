# Disease Prediction System

An AI-powered healthcare application that predicts potential diseases based on user-selected symptoms using machine learning. It combines Random Forest, XGBoost, and LightGBM through soft voting to generate disease predictions and confidence scores.

> **Disclaimer:** This application is intended for educational and informational purposes only. Predictions are not medical diagnoses and should not replace professional medical advice, diagnosis, or treatment.

## Features

- Search and select multiple symptoms
- Ensemble machine learning model using soft voting
- Top 3 disease predictions with confidence scores
- Symptom-based disease classification
- Suggested next steps based on prediction results
- REST API powered by Flask
- Responsive web interface
- Prediction pipeline for real-time results

## How It Works

1. **Symptom Selection:** Users search for and select symptoms through the web interface.
2. **Data Processing:** Selected symptoms are converted into a binary feature vector.
3. **Disease Prediction:** An ensemble voting classifier combines Random Forest, XGBoost, and LightGBM.
4. **Results:** The application displays the top 3 predicted diseases, confidence scores, matched symptoms, and suggested actions.

## Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- Flask
- Flask-CORS
- REST APIs

**Machine Learning**
- Scikit-learn
- XGBoost
- LightGBM
- Pandas
- NumPy

## Project Structure

```text
Diseases-Prediction-based-on-Symptoms/
├── Dataset/
├── static/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── app.py
├── train_combine.py
├── symptoms_list.json
├── diseases_list.json
├── model_info.json
├── classification_report.txt
├── confusion_matrix.png
├── feature_importance.png
├── requirements.txt
└── README.md
```

*Note: `model.pkl` and other generated pickle files are not included in Git because of their size. The model must be generated locally before running the application.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/gaurangmishra1/Diseases-Prediction-based-on-Symptoms.git
cd Diseases-Prediction-based-on-Symptoms
```

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib seaborn scikit-learn xgboost lightgbm flask flask-cors
```

### 4. Generate the machine learning model

Make sure the required CSV datasets are present in the `Dataset` folder. Then run:

```bash
python train_combine.py
```

Wait for training to complete. This generates the model files needed by the application and may require substantial disk space and memory.

### 5. Start the application

```bash
python app.py
```

Open the following URL in your browser:

http://127.0.0.1:5000

## Key Highlights

- Ensemble learning using three machine learning algorithms
- Multi-class disease classification
- Flask-based prediction API
- Interactive symptom selection
- User-friendly healthcare assistance interface

## Future Enhancements

- Cloud deployment
- Mobile application support
- Deep learning-based disease prediction
- Doctor recommendation system
- Personalized health analytics dashboard

## Author

**Gaurang Mishra**

