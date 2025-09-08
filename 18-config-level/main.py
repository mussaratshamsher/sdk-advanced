# main file of checking and Testing config settings

from agents import Runner, set_tracing_disabled, RunConfig, setdefault_openai_client
from my_agent.teacher_agents import gemini_agent, groq_agent

from my_config.gemini_config import GEMINI_MODEL,gemini_client
from my_config.groq_config import GROQ_MODEL,groq_client


# Golbal config
## set_default_openai_api("chat_completions") # This function is not defined/imported
set_default_openai_client(gemini_client)

# Set it to use gemini api key and model
set_tracing_disabled(True)

res = Runner.run_sync(
    starting_agent=gemini_agent,
    input="2+3=?",
    run_config=RunConfig(model=GEMINI_MODEL,       #runner level config
             model_provider=gemini_client)
)

print(res.final_output)