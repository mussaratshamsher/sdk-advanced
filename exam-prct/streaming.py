import asyncio
import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv
from agents.run import RunConfig

load_dotenv()

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

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

assistant = Agent(
    name="Personal Assistant",
    instructions="You are a helpful personal assistant."
)

async def main():
    user_input = input("Prompt: ")

    result = Runner.run_streamed(
        assistant,
        [{"role": "user", "content": user_input}],
        run_config=config
    )

    print("Assistant: ", end="", flush=True)

    async for event in result.stream_events():
        if event.type == "raw_response_event" and hasattr(event.data, "delta"):
            token = event.data.delta
            print(token, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
