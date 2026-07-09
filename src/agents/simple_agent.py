from agent_framework import Agent
import asyncio
import os
from src.config.settings import *

agent=Agent(
    name="HelloAgent",
    instructions="You are a friendly assistant.Keep your answers brief.",
    client=foundry_client, 
)