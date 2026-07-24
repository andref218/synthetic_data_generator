# Synthetic Data Generator

An AI-powered application for generating realistic synthetic datasets using Large Language Models (LLMs).

This project explores two different approaches to LLM inference:

- **Hugging Face** – Local inference using open-source models.
- **OpenAI** – Cloud inference with OpenAI models or local inference using Ollama.

---

# Hugging Face Implementation

Generate realistic synthetic datasets using open-source language models running locally with Hugging Face Transformers.

## Screenshot

![Hugging Face Demo](screenshots/synthetic_data_generator_hugging_face_models.png)

## Features

- Local inference using Hugging Face Transformers
- Supports multiple open-source LLMs
  - Google Gemma 2B
  - Qwen 2.5 3B
- Gradio web interface
- CSV dataset generation
- JSON dataset generation

---

# OpenAI Implementation

Generate realistic synthetic datasets using cloud-hosted OpenAI models or locally hosted Ollama models through the OpenAI-compatible API.

## Screenshot

![OpenAI Demo](screenshots/synthetic_data_generator_openai_models.png)

## Features

- OpenAI GPT-4o Mini integration
- Local inference using Ollama (Llama 3.2)
- Switch between cloud and local models
- Gradio web interface
- CSV dataset generation
- JSON dataset generation

---

# Project Structure

```text
synthetic-data-generator/
│
├── huggingface/
│   ├── app.py
│   ├── config.py
│   ├── generator.py
│   ├── prompts.py
│   ├── requirements.txt
│   └── .env.example
│
├── openai/
│   ├── app.py
│   ├── config.py
│   ├── generator.py
│   ├── prompts.py
│   ├── requirements.txt
│   └── .env.example
│
└── screenshots/
```

# Installation

Clone the repository:

```bash
git clone https://github.com/andref218/synthetic_data_generator.git
cd synthetic_data_generator
```

---

## Hugging Face Version

Navigate to the Hugging Face implementation:

```bash
cd huggingface
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## OpenAI / Ollama Version

Navigate to the OpenAI implementation:

```bash
cd openai
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

If using Ollama, install Ollama:

https://ollama.com

Download the language model:

```bash
ollama pull llama3.2
```

Run the application:

```bash
python app.py
```

# Configuration

Create a `.env` file based on `.env.example`.

### Hugging Face

```text
HF_TOKEN=your_huggingface_token
```

### OpenAI

```text
OPENAI_API_KEY=your_openai_api_key
```

---

# Usage

1. Select the output format (CSV or JSON).
2. Enter a description of the dataset.
3. Choose the language model.
4. Generate the synthetic dataset.

---

# Technologies

- Python
- Gradio
- Hugging Face Transformers
- OpenAI API
- Ollama
- PyTorch
