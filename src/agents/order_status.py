from agent_framework import Agent
from src.config.settings import *
from src.tools.order_status import get_order_status
from src.middleware.function_middleware import  tool_logging_middleware 
assistant=Agent(
    name="Assistant",
    instructions="""
    You are a helpful assistant.Keep you answers brief and use when need
    For order-related queries, always use the get_order_status tool instead of guessing.
    """,
    client=foundry_client,
    tools=[get_order_status],
    middleware=[tool_logging_middleware],
)