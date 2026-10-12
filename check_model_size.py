
import os
import pickle

model_path = "model.pkl"

print("Model file size:", round(os.path.getsize(model_path) / (1024 ** 3), 2), "GB")

with open(model_path, "rb") as f:
    model = pickle.load(f)

for name, estimator in model.named_estimators_.items():
    print(f"{name}: {type(estimator).__name__}")
    print("  Number of features:", getattr(estimator, "n_features_in_", "N/A"))
    print("  Number of classes:", len(getattr(estimator, "classes_", [])))
