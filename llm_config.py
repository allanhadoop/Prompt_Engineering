import os
import ollama
from openai import OpenAI
from dotenv import load_dotenv
import openai 
# Load environment variables
load_dotenv()

# Configuration
API_KEY = os.getenv("OLLAMA_API_KEY")
MODEL = "llama3.2:1b"
OLLAMA_BASE_URL = "http://localhost:11434/v1"

# Create Ollama client
ollama = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key=API_KEY
)