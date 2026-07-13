from agent_framework import Agent
from src.config.settings import foundry_client
data_agent=Agent(
    name="Data Agent",
    instructions="""
    Retrieve factual information and statistics.
    Return only structured factual data.
    """,
    client=foundry_client,
)