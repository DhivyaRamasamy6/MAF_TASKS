from agent_framework import Agent,InMemoryHistoryProvider
import asyncio
from src.config.settings import foundry_client
from src.tools.rag_tool import search_hr_policy
from src.rag.ingestion import ingest_hr_policy
PDF=r"C:\Users\Dhivya\OneDrive - CONVERSE Data Solutions\Microsoft_Agent_Framework\data\HRPolicy.pdf"
agent=Agent(
    name="HR Policy Agent",
    client=foundry_client,
    instructions="""
    You are an HR policy assistant.

    Always use the search_hr_policy tool whenever
    the user asks about company policies,
    leave, attendance, payroll,
    benefits, holidays, insurance,
    work from home,
    or any HR-related topic.

    Answer ONLY from the retrieved context.

    If the context doesn't contain the answer,
    say that you couldn't find it.

    Always mention the page number
    and document name in your answer.
    """,
    tools=[search_hr_policy],
    context_providers=[
        InMemoryHistoryProvider(
            "memory",
            load_messages=True
        )]
)

async def main(): 
    session=agent.create_session()
    while True:
        await ingest_hr_policy(
            pdf_path=PDF,
            backend="in_memory",
        )

        query=input("query:")
        if query.lower()=="exit":
            break
        response=await agent.run(
            query,
            session=session,
        )
        print("Agent:",response)
if __name__=="__main__":
    asyncio.run(main())