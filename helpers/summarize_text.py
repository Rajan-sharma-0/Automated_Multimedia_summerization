# helpers/summarize_text.py

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

_MODEL_NAME = "facebook/bart-large-cnn"
_DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

_tokenizer = AutoTokenizer.from_pretrained(_MODEL_NAME)
_model = AutoModelForSeq2SeqLM.from_pretrained(_MODEL_NAME).to(_DEVICE)

def summarize_text(text: str, max_length: int = 130, min_length: int = 30) -> str:
    inputs = _tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    ).to(_DEVICE)

    with torch.no_grad():
        output_ids = _model.generate(
            **inputs,
            max_length=max_length,
            min_length=min_length,
            num_beams=4,
            early_stopping=True
        )

    return _tokenizer.decode(output_ids[0], skip_special_tokens=True)
