from agent_framework import Agent
import asyncio
import os
from src.memory.db_stroage.history_provider import PostgreHistoryProvider
from src.memory.db_stroage.db_service import ConversationDB
from src.config.settings import *
# from src.common.logger import get_logger
# logger=get_logger(__name__)
from src.tools.hrms_tool import hrms_tool
db=ConversationDB()
history_provider=PostgreHistoryProvider(db)
agent=Agent(
    name="HelloAgent",
    instructions="""You are a helpful assistant.Keep your answers brief.""",
    client=foundry_client,
    context_providers=[history_provider],
)
agent1=Agent(
    name="HelloAgent",
    instructions="""You are a friendly assistant.Keep your answers brief.
    Responsibilities:
            - Use get_employee to retrieve employee details by employee ID.
            - Use list_employees when the user requests all employees.
            - Use search_employee when the user searches by employee name.
            - Use get_department_employees when the user requests employees from a specific department.
        
            Rules:
            - Always use the appropriate MCP tool.
            - Never fabricate employee information.
            - If no records are found, clearly inform the user.
            - Ask for clarification if the request is ambiguous.
        
        Respond professionally and concisely.""",
    tools=[hrms_tool],
    client=openai_client, 
   
  
)
agent2=Agent(
    name="HelloAgent",
    instructions="""You are a friendly HR assistant.Keep your answers brief.
    Responsibilities:
        - Use get_employee to retrieve employee details by employee ID.
        - Use list_employees when the user requests all employees.
        - Use search_employee when the user searches by employee name.
        - Use get_department_employees when the user requests employees from a specific department.
    
        Rules:
        - Always use the appropriate MCP tool.
        - Never fabricate employee information.
        - If no records are found, clearly inform the user.
        - Ask for clarification if the request is ambiguous.
    
    Respond professionally and concisely.
    """,
    client=openai_completion_client, 
    tools=hrms_tool,
  
)
# session=agent.create_session()
session=agent.get_session(session_id="d59db7b3-679e-4a3d-bb35-afc768c7d80a",service_session_id=None)
print("Session Id: ",session.session_id)
async def main():
    while True:
        query=input("query : ",)
        if query.lower=="exit":
            break
        result=await agent.run(
                        query,session=session
                    )
        print(result)
    # result= await agent.run("What is the largest city in France?.")
    # print(f"Agent: {result}")
#     # Turn 1
#             result = await agent2.run(
#                 "My name is Goku.",
#                 session=session,
#             )
#             print("Assistant:", result.text)

#             # Turn 2
#             result = await agent2.run(
#                 "What is my name?",
#                 session=session,
#             )
#             print("Assistant:", result.text)

#             # Turn 3
#             result = await agent2.run(
#                 "Remember that I am learning Microsoft Agent Framework.",
#                 session=session,
#             )
#             print("Assistant:", result.text)

#             # Turn 4
#             result = await agent2.run(
#                 "What am I learning?",
#                 session=session,
#             )
#             print("Assistant:", result.text)
        
asyncio.run(main())
