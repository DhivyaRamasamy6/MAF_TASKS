from agent_framework import Agent
from src.config.settings import *
from src.prompts.prompt import data_engineering
data_engineering_assistant=Agent(
    name="DataEngineering Assistant",
    instructions=data_engineering,
    client=openai_client,
)