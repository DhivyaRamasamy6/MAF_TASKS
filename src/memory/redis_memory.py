from agent_framework.redis import RedisHistoryProvider
import asyncio
import os
from src.config.settings import foundry_client
from agent_framework import Agent,AgentSession
import json
REDIS_URL="redis://localhost:6379"  #from docker hub
# docker --version
# docker pull redis:latest
# docker run -d -p 6379:6379 --name redid-basic redis:latest
# docker ps
# docker exec -it redid-basic redis-cli ping
redis_provider=RedisHistoryProvider(
    source_id="redis_basic_chat",
    redis_url=REDIS_URL,
)
    
agent=Agent(
    name="RedisAgent",
    client=foundry_client,
    instructions="You are a helpful assistant that remembers our conversation using Redis.",
    context_providers=[redis_provider],
)
session=agent.create_session()
async def main():
    while True:
        query=input("Enter query: ")
        
        if query.lower()=="serialize":
            serialized=session.to_dict()
            print("serialized session")
            print(json.dumps(serialized))

            resumed = AgentSession.from_dict(serialized)
            r = await agent.run("What have we talked about so far?", session=resumed)
            print(f"Agent (resumed session): {r.text}\n")
            continue
        if query=="exit":
            break
    
        result=await agent.run(
            query,session=session
        )
        print(result.text)
        
asyncio.run(main())