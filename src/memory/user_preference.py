from agent_framework import ContextProvider,AgentSession,SessionContext
from typing import Any
from agent_framework import  Agent
from src.config.settings import foundry_client
import asyncio
class UserPreferenceMemoryProvider(ContextProvider):
    """A context provider that remembers the user info in sesion state."""
    DEFAULT_SOURCE_ID="user_preferences"
    def __init__(self):
        super().__init__(self.DEFAULT_SOURCE_ID)
    async def before_run(self,*,agent:Any,session:AgentSession|None,context:SessionContext,state:dict[str,Any])->None:
        """Inject personalization instructions based on stored user info."""
        report_format=state.get("report_format")
        if report_format:
            context.extend_instructions(
                self.source_id,
                f"The user's  preferred report format is {report_format}.Always use this format unless the user asks to change it.",
            )
        
    async def after_run(
        self,*,agent:Any,session:AgentSession|None,context:SessionContext,state:dict[str,Any],
        )->None:
        """Extract and store user info in session state after each call."""
        for msg in context.input_messages:
            text=msg.text if hasattr(msg,"text") else ""
            if not isinstance(text,str):
                continue
            
            text_lower=text.lower()
            if "preferred report format is" in text_lower:
                report_format=(text_lower.split("preferred report format is")[-1].strip().split()[0].upper())
                state["report_format"]=report_format
            elif "i prefer" in text_lower:
                if "pdf" in text_lower:
                    state["report_format"]="PDF"
                elif "excel" in text_lower:
                    state["report_format"]="Excel"
                elif "word" in text_lower:
                    state["report_format"]="word"
            
# agent=Agent(
#     name="PreferenceAgent",
#     client=foundry_client,
#     instructions="""
#     You are a context-aware assistant.

#     Only answer questions using the information provided by the context providers.

#     Do not use your general knowledge or make assumptions.
# """,
#     context_providers=[UserPreferenceMemoryProvider()],
# )
# session = agent.create_session()
# async def main():
   
#     result = await agent.run("What is AI?", session=session)
#     print(f"Agent: {result}\n")

#     #user preference
#     result = await agent.run("My preferred report format is PDF.", session=session)
#     print(f"Agent: {result}\n")

    
#     provider_state = session.state.get("user_preferences", {})
#     print(f"[Session State] Stored user preference: {provider_state.get('report_format')}")
# asyncio.run(main())