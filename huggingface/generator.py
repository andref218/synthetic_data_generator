from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from config import MODELS, quant_config
from prompts import build_prompt


def load_model(model_name):
    """Load a Hugging Face model and tokenizer."""
    print(f"Loading {model_name}...")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    if torch.cuda.is_available():
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            quantization_config=quant_config
        )
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_name
        )


    return tokenizer, model


def generate_dataset(dataset_description, rows, output_format, tokenizer, model):
    """Generate a synthetic dataset using the selected LLM."""

    # Build the prompt
    prompt = build_prompt(dataset_description, rows, output_format)

    # Convert the prompt into model input tokens
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        return_tensors="pt",
        add_generation_prompt=True
    ).to(model.device)

    # Generate the model response
    outputs = model.generate(
        inputs,
        max_new_tokens=1024,
        temperature=0.7,
        do_sample=True
    )

    # Decode the generated tokens back into text
    generated_tokens = outputs[0][inputs.shape[-1]:]

    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    return response

def generate(dataset_description, rows, output_format, selected_model):
    """Gradio entry point."""
    tokenizer, model = load_model(MODELS[selected_model])

    dataset = generate_dataset(
        dataset_description,
        rows,
        output_format,
        tokenizer,
        model
    )

    return dataset