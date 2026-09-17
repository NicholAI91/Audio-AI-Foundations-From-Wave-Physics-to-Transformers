import librosa
import librosa.display
import matplotlib.pyplot as plt

audio, sr = librosa.load("sample.wav")

D = librosa.stft(audio)

plt.figure(figsize=(10, 4))

librosa.display.specshow(
    librosa.amplitude_to_db(abs(D)),
    sr=sr,
    x_axis="time",
    y_axis="log"
)

plt.colorbar()
plt.title("STFT Spectrogram")
plt.tight_layout()

plt.show()
