import torch
from transformers import ASTForAudioClassification

model = ASTForAudioClassification.from_pretrained(
    "MIT/ast-finetuned-audioset"
)

print(model)
