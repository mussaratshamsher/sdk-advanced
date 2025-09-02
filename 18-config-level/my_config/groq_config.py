import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI


load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
base_url = "https://api.groq.com/openai/v1"

groq_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=base_url
)

GROQ_MODEL = OpenAIChatCompletionsModel(
    model="llama-3.3-70b-versatile",
    openai_client=groq_client
)