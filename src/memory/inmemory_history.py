from agent_framework import Agent,InMemoryHistoryProvider,AgentSession
from src.config.settings import foundry_client
import asyncio
import json
agent1=Agent(
    name='Storage Agent',
    instructions="You are a helpful assistant",
    context_providers=[InMemoryHistoryProvider("memory",load_messages=True)],
    client=foundry_client,
    
)
session=agent1.create_session()
print("Session ID: ",session.session_id)

async def main():
   
    while True:
        query=input("Enter query: ")
        
        if query.lower()=="serialize":
            serialized=session.to_dict()
            print("serialized session")
            print(json.dumps(serialized))

            resumed = AgentSession.from_dict(serialized)
            r = await agent1.run("What have we talked about so far?", session=resumed)
            print(f"Agent (resumed session): {r.text}\n")
            continue
        if query=="exit":
            break
    
        result=await agent1.run(
            query,session=session
        )
        print(result.text)
    
asyncio.run(main())
    
