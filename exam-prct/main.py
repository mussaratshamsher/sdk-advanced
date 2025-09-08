import asyncio
from agents import Agent, Runner
from config.config import model


assistant = Agent(
    name="Story Writer", model=model,
    instructions="You are helpful assisstant that answers users prompts and  if needed you use tools to answer properly.",

)

async def main():
    user_input = input("write your question:")
    result = await Runner.run(assistant, user_input)
    print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main())
