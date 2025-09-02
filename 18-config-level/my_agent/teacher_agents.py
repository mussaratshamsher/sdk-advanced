from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL    


gemini_agent = Agent(
    name="Ali Baba",
    instructions="You are a helpful assistant.",
    model=GEMINI_MODEL,
)

groq_agent = Agent(
    name="Mussarat",
    instructions="you are a helpful assistant.",
    model=GROQ_MODEL,
)