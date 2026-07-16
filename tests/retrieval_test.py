import asyncio
from src.rag.retrieval import retrieve_hr_policy
from src.rag.ingestion import ingest_hr_policy

PDF = r"C:\Users\Dhivya\OneDrive - CONVERSE Data Solutions\Microsoft_Agent_Framework\data\HRPolicy.pdf"

async def main():

    await ingest_hr_policy(
        pdf_path=PDF,
        backend="in_memory",
    )

    chunks = await retrieve_hr_policy(
        query="leave policy",
        backend="in_memory",
        top=3,
    )

    print("Retrieved:", len(chunks))

    for chunk in chunks:
        print(chunk.section_title)
        print(chunk.content[:200])

asyncio.run(main())