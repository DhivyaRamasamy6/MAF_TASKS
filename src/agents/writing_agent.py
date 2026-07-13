from agent_framework import Agent
from src.config.settings import foundry_client

writing_agent=Agent(
    name="Writing Agent",
    instructions= """
    Convert structured information into
    professional reports.
    """,
    client=foundry_client,
)