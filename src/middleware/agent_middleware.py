import time
import uuid
from collections.abc import Awaitable,Callable
from agent_framework import AgentMiddleware,AgentContext,AgentResponse,Message
from src.models.ollama_classifier import classify_request
from src.common.logger import get_logger
logger=get_logger(__name__)
class RequestLoggingAgentMiddleware(AgentMiddleware):
    """Agent middleware that logs execution."""
    logger.info("[RequestLoggingAgentMiddleware] processing")
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
       logger.info("[RequestLoggingAgentMiddleware] processed")
       print(f"Execution Time : {end:.2f} sec")
       
       
       
class FinanceValidationMiddleware(AgentMiddleware):
    """
    Validates finance-related requests.

    Extracts the user's query, classifies it to determine the user's role
    and request category, and blocks finance requests from users whose
    role is not 'Finance'.
    
    """
    logger.info("[FinanceValidationMiddleware] processing")
    async def process(
        self,
        context:AgentContext,
        call_next:Callable[[],Awaitable[None]],
    )->None:
       user_query=context.messages[-1].text.lower()
       result=await classify_request(user_query)
       role=result.role.lower()
       category=result.category.lower()
       print(result)
       if category=="finance" and role!="finance":
           context.result=AgentResponse(messages=[Message(role="assistant",contents=['Access Denied. Only Finance users can access finance information.'],)])
           return
       logger.info("[FinanceValidationMiddleware] processed")
       await call_next()