from src.config.settings import foundry_client
import asyncio
from agent_framework import Agent
file_search_tool = foundry_client.get_file_search_tool(
    vector_store_ids=[""]
)


agent = Agent(
    client=foundry_client,
    instructions="Answer questions using the uploaded documents.",
    tools=[file_search_tool],
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