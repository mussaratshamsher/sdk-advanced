
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, ModelSettings, function_tool, set_tracing_disabled
import asyncio

set_tracing_disabled(True)
load_dotenv()

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
#agent
assistant = Agent(
    name="Essay Writer", model=model,
    instructions="You are helpful assisstant that answers users prompts.",
)
user_input = "write 5 lines about the importance of time management"
result = asyncio.run(Runner.run(assistant, user_input))
print(result.final_output)
# async def main():

#     user_input = input("write your question:")
#     result = await Runner.run(assistant, user_input)
#     print(result.final_output)
       
# if __name__ == "__main__":
#     asyncio.run(main())

