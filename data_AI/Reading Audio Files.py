import librosa
import numpy as np
import os

def load_audio_file(file_path, sr=16000):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File does not exist: {file_path}")
    audio, sample_rate = librosa.load(file_path, sr=sr)
    return audio, sample_rate

audio_data, sr = load_audio_file(r"audio.wav.mp3")
print(f"Loaded audio with {len(audio_data)} samples at {sr} Hz")
print(f"Waveform shape: {audio_data.shape}")
