from config import MODELS, openai, ollama
from prompts import build_prompt


def generate_dataset(dataset_description, rows, output_format, model, client):
    """Generate a synthetic dataset using the selected LLM."""

    prompt = build_prompt(
        dataset_description,
        rows,
        output_format
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an expert synthetic data generator."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


def generate(dataset_description, rows, output_format, selected_model):
    """Gradio entry point."""

    model = MODELS[selected_model]

    client = ollama if selected_model == "Llama 3.2" else openai

    dataset = generate_dataset(
        dataset_description,
        rows,
        output_format,
        model,
        client
    )

    return dataset