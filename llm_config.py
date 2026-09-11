import os
import ollama
from openai import OpenAI
from dotenv import load_dotenv
import openai 
load_dotenv(override=True)

#----------- Ollama -----------------------------
API_KEY = os.getenv("OLLAMA_API_KEY")
MODEL_OLLAMA = "llama3.2:1b"
OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key=API_KEY
)

#------------Groq------------
groq_api_key = os.getenv("GROQ_API_KEY")
groq_url = "https://api.groq.com/openai/v1" 
MODEL_GROQ = "openai/gpt-oss-120b"
groq = OpenAI(
    base_url=groq_url,
    api_key=groq_api_key 
)
