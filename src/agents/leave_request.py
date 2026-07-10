from agent_framework import Agent,Message
from src.tools.leave_request import submit_leave_request
from src.config.settings import foundry_client
import asyncio
leave_agent=Agent(
    name="Leave Approval Assistant",
    instructions="""
    You are a Leave Approval Assistant.

When the user requests leave:

1. Collect all required information.
2. Call the submit_leave_request tool.
3. If tool approval is requested, wait.
4. Once approval is received, execute the approved tool immediately.
5. Do not ask for confirmation again after approval.
6. Never approve leave yourself.
    """,
    tools=[submit_leave_request],
    client=foundry_client,
)

async def main():
    session=leave_agent.create_session()
    user_query=input("Enter query: ")
    result=await leave_agent.run(user_query,session=session)
    while result.user_input_requests:
        
        pending=result.user_input_requests[0]
        print("pending: ",pending)
        print("Tool Approval Needed")
        print("Tool:",pending.function_call.name)
        print("Arguments:",pending.function_call.arguments)
        approve=input("Approve (Y/N):").lower()=="y"
        approve_response=pending.to_function_approval_response(approve)
        result=await leave_agent.run(
            Message("user",[approve_response]),
            session=session
        )
        
        print("Final Response")
        print(result.text)
    else:
        result=await leave_agent.run(
            user_query
        )
        print("Without Human intervention:",result.text)
asyncio.run(main())