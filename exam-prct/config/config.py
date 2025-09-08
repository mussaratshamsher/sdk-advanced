
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled


# Disable tracing and enable verbose stdout for debugging
set_tracing_disabled(True)
load_dotenv()

# Setup Gemini model
API_KEY = os.getenv("GEMINI_API_KEY")
external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash-latest",  # Corrected to a valid model name
    openai_client=external_client
)