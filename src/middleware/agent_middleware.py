import time
import uuid
from collections.abc import Awaitable,Callable
from agent_framework import AgentMiddleware,AgentContext

class RequestLoggingAgentMiddleware(AgentMiddleware):
    """Agent middleware that logs execution."""
    async def process(
        self,
        context: AgentContext,
        call_next: Callable[[], Awaitable[None]],
    ) -> None:
       user_id=str(uuid.uuid4())
       request_id=str(uuid.uuid4())
       start=time.perf_counter() 
       context.metadata["request_id"]=request_id
       context.metadata["user_id"]=user_id
       print(f"Request ID:{request_id}")
       print(f"User ID:,{user_id}")
       await call_next()
       end=time.perf_counter()-start
       
       print(f"Execution Time : {end:.2f} sec")
       
