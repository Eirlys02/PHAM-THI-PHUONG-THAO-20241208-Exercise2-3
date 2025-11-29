import librosa

def extract_mfcc(audio, sr=16000, n_mfcc=13):
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    return mfccs

audio_data, sr = librosa.load("audio.wav.mp3", sr=16000)
mfcc_features = extract_mfcc(audio_data, sr)
print("MFCC shape:", mfcc_features.shape)
