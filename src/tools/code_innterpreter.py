from agent_framework import Agent, Content
from src.config.settings import openai_client
import asyncio
async def main() -> None:
    """Example showing how to use the code interpreter tool with OpenAI Chat."""
    print("=== OpenAI Chat Client Agent with Code Interpreter Example ===")

    client = openai_client
    agent = Agent(
        client=client,
        instructions="You are a helpful assistant that can write and execute c code to solve problems.",
        tools=client.get_code_interpreter_tool(),
    )

    query = "Use code to get the factorial of 100?"
    print(f"User: {query}")
    result = await agent.run(query)
    print(f"Result: {result}\n")

    for message in result.messages:
        code_blocks = [c for c in message.contents if c.type == "code_interpreter_tool_call"]
        outputs = [c for c in message.contents if c.type == "code_interpreter_tool_result"]

        if code_blocks:
            code_inputs = code_blocks[0].inputs or []
            for content in code_inputs:
                if isinstance(content, Content) and content.type == "text":
                    print(f"Generated code:\n{content.text}")
                    break
        if outputs:
            print("Execution outputs:")
            for out in outputs[0].outputs or []:
                if isinstance(out, Content) and out.type == "text":
                    print(out.text)


if __name__ == "__main__":
    asyncio.run(main())
