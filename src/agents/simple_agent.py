from agent_framework import Agent
import asyncio
import os
from src.config.settings import *
from src.memory.custom_mem import InMemoryHistory
from src.middleware.agent_middleware import RequestLoggingAgentMiddleware
from src.middleware.chat_middleware import TokenLoggingMiddleware,pii_masking_middlewalre
from src.memory.user_context import UserContextProvider
from src.middleware.agent_middleware import FinanceValidationMiddleware
from src.common.logger import get_logger
from src.tools.weather import get_weather
from src.tools.calculator import calculator
from src.middleware.function_middleware import SafeToolMiddleware,ToolCallRateLimitingMiddleware
from src.tools.github_tool import github_mcp
logger=get_logger(__name__)

agent=Agent(
    name="HelloAgent",
    instructions="""
    You are a Customer Support Assistant.

    Keep your responses brief and professional.

    Always use the appropriate tool:

    - Use get_weather to retrieve weather information.
    - Use calculator to retrieve math information.
    - Use the github_mcp to search repositories, read files, check issues, and perform GitHub operations.

        """,
   
    tools= [
    get_weather,
    calculator,
    github_mcp(),
    ],
    client=foundry_client,

)
# middleware=[ToolCallRateLimitingMiddleware(),RequestLoggingAgentMiddleware(),TokenLoggingMiddleware()],
session=agent.create_session()
print("Session ID:" ,session.session_id)
async def main():
    while True:
        query=input("query:")
        if query.lower()=="exit":
            break
        
        response=await agent.run(
            query,
            session=session,
           
        )
        
        print("Agent:",response)
asyncio.run(main())

# history=InMemoryHistory()
# async def main():
#     while True:
#         user_msg=input("Enter input : ")
#         if user_msg.lower()=="exit":
#             break
#         history.add_message(session.session_id,"user",user_msg)
        
#         result=await agent.run(
#             user_msg,session=session
#         )
#         history.add_message(session.session_id,"assistant",result.text)
#         print("Agent :",result.text)
# asyncio.run(main())

# print("History \n",history.get_history(session.session_id))