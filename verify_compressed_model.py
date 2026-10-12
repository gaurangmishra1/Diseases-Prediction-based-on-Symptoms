
import gzip
import pickle
import os

print("Verifying compressed model...")

with gzip.open("model.pkl.gz", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully!")

for name, estimator in model.named_estimators_.items():
    print(f"{name}: {type(estimator).__name__}")

print("Compressed file size:",
      round(os.path.getsize("model.pkl.gz") / (1024 ** 2), 2), "MB")
