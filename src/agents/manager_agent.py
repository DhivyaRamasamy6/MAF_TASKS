from agent_framework import Agent
from src.config.settings import foundry_client
from src.agents.data_agent import data_agent
from src.agents.writing_agent import writing_agent

manager_agent=Agent(
    name="Manager Agent",
    instructions="""
        Coordinate specialized agents.

        Use Data Agent whenever factual
        information is required.

        Use Writing Agent whenever
        content writing is required.
    """,
    client=foundry_client,
    tools=[data_agent.as_tool(),writing_agent.as_tool()],
)
