#Build a “Company Assistant” that answers only from its instructions and streams the response.
from agent_framework import Agent
from src.config.settings import client
import asyncio
agent =Agent(
     name="Company Assistant",
     instructions="""
        You are Company Assistant for ABC Technologies.

        Company Information:
        - Founded: 2020
        - Headquarters: Chennai, India
        - Business: AI and Data Solutions
        - Working Hours: Monday to Friday, 9:00 AM–6:00 PM
        - Support Email: support@abctech.com
        - HR Email: hr@abctech.com
        - Products:
        - AI Chatbot Platform
        - Document Intelligence
        - Data Analytics Dashboard

        Instructions:
        - Answer only using the company information above.
        - Do not use external knowledge.
        - If the answer is not available, reply:
        "I'm sorry, I don't have information about that."
        - Be professional and concise.
     """,
    client=client,
)

async def main():
    while True:
        query=input("Enter input: ")
        if query == "exit":
            break
        #streaming
        async for chunk in agent.run(query,stream=True):
            print(chunk.text,end="",flush=True)
        print()
asyncio.run(main())
    
