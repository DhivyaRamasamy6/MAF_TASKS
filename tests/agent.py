from agent_framework import Agent
import asyncio
import os
from src.config.settings import client
# from src.common.logger import get_logger
# logger=get_logger(__name__)
agent=Agent(
    name="HelloAgent",
    instructions="You are a friendly assistant.Keep your answers brief.",
    client=client, 
)

async def main():
   
    result= await agent.run("What is the largest city in France?.")
   
    print(f"Agent: {result}")
asyncio.run(main())
