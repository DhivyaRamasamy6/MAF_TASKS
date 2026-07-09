from agent_framework import Agent
from src.config.settings import *
from src.prompts.prompt import finance

finance_agent=Agent(
    name="Finance Assistant",
    instructions=finance,
    client=openai_client,
)