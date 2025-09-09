import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled

set_tracing_disabled(True)

# Correctly locate the .env file from the project root
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Setup Gemini model
API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = os.getenv("GEMINI_BASE_URL")

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)