from collections.abc import Awaitable,Callable
from agent_framework import FunctionInvocationContext,FunctionMiddleware
import time
from src.common.logger import get_logger
logger=get_logger(__name__)
async def tool_logging_middleware(
    context:FunctionInvocationContext,
    call_next:Callable[[],Awaitable[None]],
    ):
    """Logs the tool calling"""
    logger.info("[tool_logging_middleware] processing")
    print(f"Selected Tool : {context.function.name}")
    start=time.perf_counter()
    await call_next()
    end=time.perf_counter()-start
    print(f"Execution Time : {end:.2f} sec")
    print("Tool Finished")
    logger.info("[tool_logging_middleware] processed")
    
class SafeToolMiddleware(FunctionMiddleware):
    logger.info("[SafeToolMiddleware] processing")
    async def process(
        self,context:FunctionInvocationContext,call_next:Callable[[],Awaitable[None]],
    )->None:
        try:
            await call_next()
        except Exception as ex:
            print(f"Tool error: {context.function.name} -->{ex}")
            context.result=(
                "I'm sorry, I couldn't retrieve the requested information "
                "because the service is currently unavailable. "
                "Please try again later."
            )
            
class ToolCallRateLimitingMiddleware(FunctionMiddleware):
    """
    Stops agent execution when the maximum tool call limit is reached
    or when the same tool is invoked repeatedly to prevent execution loops.
    """
    logger.info("[ToolCallRateLimitingMiddleware] processing")  
    def __init__(self):
       self.tool_calls=0
       self.previous_tool=None
       self.repeat_count=0
     
    async def process(
        self,context:FunctionInvocationContext,call_next:Callable[[],Awaitable[None]],
       )->None:
        tool_name=context.function.name
        self.tool_calls+=1
        if tool_name==self.previous_tool:
            self.repeat_count+=1
        else:
            self.repeat_count=1
            self.previous_tool=tool_name
        #guardrail 1 - maximum 5 tool calls only
        if self.tool_calls>5:
            context.result(
                "Agent Stopped:Maximun tool call 5 reached."
            )
            return
        #guardrail 2 -same tool calling limit
        if self.repeat_count>=3:
            context.result=(
                f"Agent Stopped:Tool {tool_name} is being called repeatedly"
            )
            return
        await call_next()
        