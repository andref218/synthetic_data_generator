from dotenv import load_dotenv
from huggingface_hub import login
import os

import gradio as gr

from config import MODELS
from generator import generate

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found. Please create a .env file.")

login(HF_TOKEN)

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
            value="Gemma 2B",
            label="LLM Model"
        ),
    ],

    outputs=gr.Textbox(
        label="Generated Dataset",
        lines=20
    ),

    title="Synthetic Data Generator",

    description="Generate realistic synthetic datasets using Hugging Face open-source language models."
)

interface.launch()