#Build a “Company Assistant” that answers only from its instructions and streams the response.
from agent_framework import Agent
from src.config.settings import *
import asyncio
#Agent with openai provider
company_assistant1 =Agent(
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
    client=openai_client,
)


#Agent with ollama provider
company_assistant2 =Agent(
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
    client=ollama_client,
)

#agent test
async def main():
    while True:
        choices=input("select the assistant: company_assistant1 or company_assistant2:")
        if choices == "1":
            print("openai_client")
            query=input("Enter input: ")
            if query == "exit":
               break
            #streaming
            async for chunk in company_assistant1.run(query,stream=True):
                # print(type(chunk))
                print(chunk.text,end="",flush=True)
            print()
        elif choices =="2":
            print("ollama_client")
            query=input("Enter input: ")
            if query == "exit":
               break
            #streaming
            
            async for chunk in company_assistant2.run(query,stream=True):
                print(chunk.text,end="",flush=True)
            print()
        else:
            break
asyncio.run(main())
    
