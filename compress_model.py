
import gzip
import shutil
import os
import time

source = "model.pkl"
destination = "model.pkl.gz"

print("Compressing model. This may take several minutes...")
start = time.time()

with open(source, "rb") as original:
    with gzip.open(destination, "wb", compresslevel=1) as compressed:
        shutil.copyfileobj(original, compressed, length=1024 * 1024)

original_size = os.path.getsize(source) / (1024 ** 3)
compressed_size = os.path.getsize(destination) / (1024 ** 3)

print(f"Original size:   {original_size:.2f} GB")
print(f"Compressed size: {compressed_size:.2f} GB")
print(f"Time taken:      {(time.time() - start) / 60:.1f} minutes")
