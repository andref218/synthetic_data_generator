import gradio as gr

from config import MODELS
from generator import generate


interface = gr.Interface(
    fn=generate,

    inputs=[
        gr.Textbox(
            label="Dataset Description",
            placeholder="e.g. Airbnb listings in Portugal"
        ),

        gr.Slider(
            minimum=5,
            maximum=100,
            value=10,
            step=5,
            label="Number of Rows"
        ),

        gr.Dropdown(
            choices=["CSV", "JSON"],
            value="CSV",
            label="Output Format"
        ),

        gr.Dropdown(
            choices=list(MODELS.keys()),
            value="GPT-4.1 Mini",
            label="LLM Model"
        ),
    ],

    outputs=gr.Textbox(
        label="Generated Dataset", 
        lines=20
    ),

    title="Synthetic Data Generator (OpenAI)",

    description="Generate realistic synthetic datasets using OpenAI and Llama language models.",
)

interface.launch()