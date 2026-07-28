import asyncio
import warnings
from typing import Annotated
from agent_framework import Agent, FunctionInvocationContext, tool
from pydantic import Field
from src.config.settings import foundry_client
warnings.filterwarnings("ignore", category=FutureWarning)  # suppress ExperimentalWarning for brevity


@tool(approval_mode="never_require")
def factorial(n: Annotated[int, Field(description="A non-negative integer.")]) -> str:
    """Compute the factorial of n."""
    if n < 0:
        return "Error: n must be a non-negative integer."
    result = 1
    for value in range(2, n + 1):
        result *= value
    return f"{n}! = {result}"


@tool(approval_mode="never_require")
def fibonacci(n: Annotated[int, Field(description="The 0-based index in the Fibonacci sequence.")]) -> str:
    """Compute the n-th Fibonacci number."""
    if n < 0:
        return "Error: n must be a non-negative integer."
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return f"fib({n}) = {a}"


# The ctx parameter is injected by the framework and is NOT visible to the model.
@tool(approval_mode="never_require")
def load_math_tools(ctx: FunctionInvocationContext) -> str:
    """Load additional math tools (factorial, fibonacci) so they can be used."""
    ctx.add_tools([factorial, fibonacci])
    return "Loaded math tools: factorial, fibonacci. You can now call them."


async def main() -> None:
    agent = Agent(
        client=foundry_client,
        name="MathAgent",
        instructions=(
            "You are a math assistant. "
            "If you need math capabilities that are not yet available, call load_math_tools first."
        ),
        tools=[load_math_tools],  # agent starts with only the loader
    )
    print(await agent.run("What is 5 factorial?"))


asyncio.run(main())