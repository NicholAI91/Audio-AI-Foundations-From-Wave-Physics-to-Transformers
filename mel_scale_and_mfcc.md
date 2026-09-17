# Mel Spectrograms & MFCCs

Humans perceive pitch logarithmically.

Mel Scale approximates biological perception.

Pipeline:

Waveform
↓
STFT
↓
Mel Filter Bank
↓
Log Compression
↓
DCT
↓
MFCCs

MFCCs typically retain:

13–40 coefficients per frame
