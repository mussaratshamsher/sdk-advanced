
import asyncio
import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv
from agents.run import RunConfig

load_dotenv()

MODEL_NAME = "gemini-2.0-flash-latest"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# External Gemini client
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model setup
model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=external_client
)

# Run configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Agent definition
assistant = Agent(
    name="Personal Assistant",
    instructions="You are a helpful personal assistant."
)

async def main():
    history = []
    print("🤖 Assistant ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break
        

        history.append({"role": "user", "content": user_input})

        result = Runner.run_streamed(assistant, history, run_config=config)
        print("Assistant: ", end="", flush=True)

        # Stream tokens to terminal
        async for event in result.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, "delta"):
                token = event.data.delta
                print(token, end="", flush=True)

        print()  # newline after streaming ends

        # Save assistant response in history
        history.append({"role": "assistant", "content": result.final_output})

if __name__ == "__main__":
    asyncio.run(main())
