import librosa

audio, sr = librosa.load("sample.wav")

mfccs = librosa.feature.mfcc(
    y=audio,
    sr=sr,
    n_mfcc=13
)

print("MFCC Shape:", mfccs.shape)
