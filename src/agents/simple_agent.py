from agent_framework import Agent
import asyncio
import os
from src.config.settings import *
from src.memory.custom_mem import InMemoryHistory
from src.middleware.agent_middleware import RequestLoggingAgentMiddleware
from src.middleware.chat_middleware import TokenLoggingMiddleware
from src.memory.user_context import UserContextProvider
from src.middleware.agent_middleware import FinanceValidationMiddleware
# from src.middleware.agent_middleware import 
agent=Agent(
    name="HelloAgent",
    instructions="You are a friendly assistant.Keep your answers brief.Answer only questions the authenticated user is authorized to access.",
    middleware=[RequestLoggingAgentMiddleware(),TokenLoggingMiddleware(),FinanceValidationMiddleware()],
    client=foundry_client,
   
)
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