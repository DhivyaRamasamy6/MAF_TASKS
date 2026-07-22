from typing import Any
from agent_framework import Agent,AgentSession,ContextProvider,SessionContext
from src.config.settings import foundry_client
import asyncio
import re
class UserContextProvider(ContextProvider):
    DEFAULT_SOURCE_ID="user_context"
    def __init__(self):
        super().__init__(self.DEFAULT_SOURCE_ID)
    
    async def befor_run(self,*,agent:Any,session:AgentSession,context:SessionContext,state:dict[str,Any],)->None:
        role=state.get("role")
        department=state.get("department")
        access_level=state.get("access_level")
       
        if role or department or access_level:
            context.extend_instructions(
                self.source_id,
                f"""
                Current user context:
                Role:{role},
                Department:{department},
                Access Level:{access_level}
                Use this information while answering the user's questions.
                """
            )
    async def after_run(
        self,*,agent:Any,session:AgentSession | None,context:SessionContext,state:dict[str,Any],
    ) ->None:
        for message in context.input_messages:
            text=(message.text or "") if hasattr(message,"text") else ""
            if not isinstance(text,str):
                continue
            
            role_match = re.search(
            r"my role is\s+(.+?)(?=\s+and\s+my department|\s+and\s+my access|\.|$)",
            text,
            re.IGNORECASE,
            )

            department_match = re.search(
                r"my department is\s+(.+?)(?=\s+and\s+my access|\.|$)",
                text,
                re.IGNORECASE,
            )

            access_match = re.search(
                r"my access level is\s+(.+?)(?=\.|$)",
                text,
                re.IGNORECASE,
            )

            if role_match:
                state["role"] = role_match.group(1).strip().title()

            if department_match:
                state["department"] = department_match.group(1).strip().title()

            if access_match:
                state["access_level"] = access_match.group(1).strip().title()
        
# agent=Agent(
#     name="Assistant",
#     client=foundry_client,
#     instructions="""You are a context-aware assistant.

#     Only answer questions using the information provided by the context providers.

#     Do not use your general knowledge or make assumptions.
#     """,
#     context_providers=[UserContextProvider()],
# )
# session=agent.create_session()
# async def main():
#     result=await agent.run("My role is Manager, my department is Finance ,my access level is Read and Write.",session=session)
#     print("result:",result)
    
#     result=await agent.run("Tell me about myself",session=session)
#     print("agent:",result)
    
#     result=await agent.run("Change my department to AI",session=session)
#     print("agent:",result)
    
#     result=await agent.run("Tell me about myself",session=session)
#     print("agent:",result)
    
# asyncio.run(main())