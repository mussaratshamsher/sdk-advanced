
import os 
import asyncio
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from agents.run import RunConfig
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
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# multiple agent as handoffs
urdu_translator = Agent(
    name="Urdu Translator Bot",
    handoff_description="Translate English to Urdu",
    instructions="You are a helpful assistant that translates English to Urdu.",
)   
arabic_translator = Agent(
    name="Arabic Translator Bot",
    handoff_description="Translate English to Arabic",
    instructions="You are a helpful assistant that translates English to Arabic.",
)
# main agent with handoffs
triage_agent = Agent(
    name="Helper Bot", model=model,
    instructions="You are a helpful assistant that can translate English to Urdu or Arabic. If the user wants to translate to Urdu, you will handoff the conversation to the Urdu Translator Bot. If the user wants to translate to Arabic, you will handoff the conversation to the Arabic Translator Bot. If the user wants to do something else, you will respond directly.",
    handoffs=[urdu_translator, arabic_translator]
)

async def main():
    user_input = input("Enter Prompt: ")
    result = await Runner.run(triage_agent, user_input, run_config=config)
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())

