from transformers import BitsAndBytesConfig
import torch

GEMMA = "google/gemma-2-2b-it"
QWEN = "Qwen/Qwen2.5-3B-Instruct"

MODELS = {
    "Gemma 2B": GEMMA,
    "Qwen 2.5 3B": QWEN
}

quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4"
)