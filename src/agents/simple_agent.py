from agent_framework import Agent
import asyncio
import os
from src.config.settings import *
from src.memory.custom_mem import InMemoryHistory

agent=Agent(
    name="HelloAgent",
    instructions="You are a friendly assistant.Keep your answers brief.",
    client=foundry_client, 

)
session=agent.create_session()
print(session.session_id)
history=InMemoryHistory()
async def main():
    while True:
        user_msg=input("Enter input : ")
        if user_msg.lower()=="exit":
            break
        history.add_message(session.session_id,"user",user_msg)
        
        result=await agent.run(
            user_msg,session=session
        )
        history.add_message(session.session_id,"assistant",result.text)
        print("Agent :",result.text)
asyncio.run(main())

print("History \n",history.get_history(session.session_id))