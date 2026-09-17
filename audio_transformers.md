# Audio Spectrogram Transformer (AST)

Pipeline:

Audio
↓
Mel Spectrogram
↓
Patch Extraction
↓
Linear Projection
↓
Positional Encoding
↓
Transformer

Attention:

Attention(Q,K,V)
=
softmax(QK^T / √dk)V

Advantages:

- Long-range dependencies
- Speech understanding
- Music structure learning
- Environmental audio analysis
