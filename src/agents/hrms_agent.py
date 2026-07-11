from agent_framework import Agent
from src.tools.hrms_tool import hrms_tool
from src.config.settings import foundry_client
# import asyncio
hrms_agent=Agent(
    name="HR Assistant",
    instructions = """
    You are an HR Assistant for the Human Resource Management System (HRMS).

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
    client=foundry_client,
    tools=[hrms_tool],
)

# async def main():
#     while True:
#         query=input("Enter query: ")
#         if query.lower() =='exit':
#             break
        
#         result=await hrms_agent.run(
#             query
#         )
#         print(result.text)
# asyncio.run(main())