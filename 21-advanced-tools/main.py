
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig, ModelSettings, function_tool, enable_verbose_stdout_logging, set_tracing_disabled
from agents import StopAtTools
from agents.tool import function_tool
import asyncio

# Disable tracing and enable verbose stdout for debugging
set_tracing_disabled(True)
enable_verbose_stdout_logging()
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
# tool 1
@function_tool
def fetch_data(age: int, work: str, home: str, salary: float, hobby: str, detail: str) -> str:
    """
    Fetches the requested detail about Ali.    
    Returns:
        str: The requested detail value as string
    """
    data = {
        "age": "25",
        "work": "Software Developer",
        "home": "Karachi",
        "salary": "120000",
        "hobby": "Reading"
    }    
    return data.get(detail.lower(), "Detail not found")
# tool 2
@function_tool
def check_is_admin():
    # Logic to check if the user is an admin
    return True
    
    #tool 3 
@function_tool
def sum_num(a: int, b:int,
    name_override="add_numbers",
    description_override="Adds two numbers and returns the result",
    is_enabled=False  # Disable this tool by default,used for giving different rights according to users.admin or g.user
    # function can be passed as its value: is_enaled=check_is_admin
):
    """Adds the given numbers""" 
    return a+b

assistant = Agent(
    name="Story Writer", model=model,
    instructions="You are helpul assisstant that answers users prompts and  if needed you use tools to answer properly.",
    tools=[fetch_data, sum_num],
    model_settings=ModelSettings(
    ),
    # tool_use_behaviour="stop_on_first_tool"
    #only tool will be used it prompt is related to call tool
    # tool_use_behaviour=StopAtTools(stop_at_tool_names=[fetch_data])
)
prompt = input("write your question:")
result = Runner.run_sync(assistant, prompt)
print(result.final_output)

# Respone api: keeps data of statful conversation, used by default .i.e.
# Completions api: does not keep data of statful conversation



