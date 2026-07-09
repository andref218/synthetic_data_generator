# Synthetic Data Generator

An AI-powered application for generating realistic synthetic datasets using Large Language Models (LLMs).

This project explores two different approaches to LLM inference:

- **Hugging Face** – Local inference using open-source models.
- **OpenAI** – Production-oriented implementation using the Chat Completions API.

---

# Hugging Face Implementation

Generate realistic synthetic datasets using open-source language models running locally with Hugging Face Transformers.

## Features

- Local inference using Hugging Face Transformers
- Supports multiple open-source LLMs
  - Google Gemma 2B
  - Qwen 2.5 3B
- Gradio web interface
- CSV dataset generation
- JSON dataset generation

## Screenshot

![Hugging Face Demo](screenshots/synthetic_data_generador_hugging_face_models.png)

# Project Structure

```text
synthetic-data-generator/
│
├── huggingface/
│   ├── app.py
│   ├── config.py
│   ├── generator.py
│   ├── prompts.py
│   ├── utils.py
│   ├── requirements.txt
│   └── .env.example
│
├── openai/
│   ├── app.py
│   ├── config.py
│   ├── generator.py
│   ├── prompts.py
│   ├── utils.py
│   ├── requirements.txt
│   └── .env.example
│
└── screenshots/
```
