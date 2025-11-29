import csv
import numpy as np
from PIL import Image
import librosa

# ---- Utility functions ----

def load_csv(path):
    """Read metadata.csv and return a list of dictionaries."""
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def load_text_file(path):
    """Read a text file and return a list of lines."""
    with open(path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
    # Remove empty lines and newline characters
    lines = [l.strip() for l in lines if l.strip() != ""]
    return lines

def preprocess_image(img, size=(224, 224)):
    """Resize image and convert to normalized numpy array [0,1]."""
    img = img.resize(size)
    arr = np.array(img).astype("float32") / 255.0
    return arr

def load_audio_file(path, sr=16000):
    """Load an audio file with sampling rate sr."""
    audio, sr = librosa.load(path, sr=sr)
    return audio, sr

def extract_mfcc(audio, sr, n_mfcc=13):
    """Extract MFCC features and take mean across time axis."""
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    mfcc_mean = mfcc.mean(axis=1)
    return mfcc_mean

# ---- Main pipeline ----

def pipeline_run():
    # Step 1: Read metadata
    metadata = load_csv("metadata.csv")

    # Step 2: Process TEXT
    text_records = []
    for item in metadata:
        text_path = item["text_file"]
        text_lines = load_text_file(text_path)
        text_records.append(text_lines)

    # Step 3: Process IMAGE
    image_records = []
    for item in metadata:
        img_path = item["image_file"]
        img = Image.open(img_path).convert("RGB")
        arr = preprocess_image(img)
        image_records.append(arr)

    # Step 4: Process AUDIO
    audio_records = []
    for item in metadata:
        audio_path = item["audio_file"]
        audio, sr = load_audio_file(audio_path, sr=16000)
        mfcc = extract_mfcc(audio, sr)
        audio_records.append(mfcc)

    # Return all preprocessed data
    return text_records, image_records, audio_records


if __name__ == "__main__":
    text_data, img_data, audio_data = pipeline_run()
    print("Number of text samples:", len(text_data))
    print("Number of image samples:", len(img_data))
    print("Number of audio samples:", len(audio_data))

    # Print example outputs
    print("\nExample text sample 1:", text_data[0])
    print("Image sample 1 shape:", img_data[0].shape)
    print("Audio MFCC sample 1 shape:", audio_data[0].shape)

