

from dotenv import load_dotenv
import os
from transformers import logging
logging.set_verbosity_error()
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


load_dotenv()
model_name = os.getenv("MODEL_NAME", "ziaulkarim245/bart-large-cnn-Text-Summarizer")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(text: str, max_new_tokens: int = 10000, min_length: int = 25) -> str:
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        min_length=min_length,
        do_sample=False,
        forced_bos_token_id=0
    )
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary.strip()