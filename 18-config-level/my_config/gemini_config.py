import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

gemini_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=base_url
)

GEMINI_MODEL = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=gemini_client
)