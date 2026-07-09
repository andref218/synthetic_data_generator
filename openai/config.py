import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Please create a .env file.")

MODELS = {
    "GPT-4.1 Mini": "gpt-4o-mini",
    "Llama 3.2": "llama3.2:latest"
}

openai = OpenAI(api_key=OPENAI_API_KEY)

ollama = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)