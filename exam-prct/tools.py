
import os 
import asyncio
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv
from agents.tool import function_tool

load_dotenv()
set_tracing_disabled(True)


MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)    

model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=external_client
)

# tools
@function_tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@function_tool
def check_person_maturity(name: str, age: int) -> str:
    """Check if a person is an adult or a young."""
    if age >= 18:
        return f"{name} is an adult."
    else:
        return f"{name} is a young."    

assistant = Agent(
    name="Helper Bot",
    model=model,
    instructions="You are a helpful assistant that can perform basic arithmetic and check if a person is an adult or a minor.",
    tools=[add, check_person_maturity]
)
async def main():
    user_input = input("Enter Prompt: ")
    result = await Runner.run(assistant, user_input)
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())

