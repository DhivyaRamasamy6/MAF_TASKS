from agent_framework import Agent
from src.config.settings import *
from src.prompts.prompt import hr_prompt
HR_Assistant=Agent(
    name="HR Assistant",
    instructions=hr_prompt,
    client=openai_client,
)