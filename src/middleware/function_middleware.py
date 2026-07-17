from collections.abc import Awaitable,Callable
from agent_framework import FunctionInvocationContext
import time
async def tool_logging_middleware(
    context:FunctionInvocationContext,
    call_next:Callable[[],Awaitable[None]],
    ):
    """Logs the tool calling"""
    print(f"Selected Tool : {context.function.name}")
    start=time.perf_counter()
    await call_next()
    end=time.perf_counter()-start
    print(f"Execution Time : {end:.2f} sec")
    print("Tool Finished")