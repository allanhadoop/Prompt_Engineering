from llm_config import MODEL, ollama
from openai import OpenAI
import ollama
from doctest import register_optionflag
from llm_config import ollama, MODEL

history = [{"role":"user", "content" : "what country is richest in the world"}]
response = ollama.responses.create(
        model = MODEL, 
        input = history,
        store = False   # Donot stoe conversation automatically
)
print("Richest country: ", response.output_text)

history += [{"role" : old.role, "content" : old.content} for old in response.output]    # add context to the first prompt
history.append({"role":"user", "content" : "what country is the poorest"})

second_response = ollama.responses.create(
        model = MODEL, 
        input = history,
        store = False
)

print("second resoponse - poor:", second_response.output_text)