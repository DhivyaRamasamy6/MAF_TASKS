import asyncio
from src.rag.ingestion import build_hr_policy_chunks, get_collection, populate_collection,ingest_hr_policy
PDF=r"C:\Users\Dhivya\OneDrive - CONVERSE Data Solutions\Microsoft_Agent_Framework\data\HRPolicy.pdf"

async def main1():
    count=await ingest_hr_policy(
        pdf_path=PDF,
        backend="in_memory",
    )
    print(f"{count} chunks uploaded.")

asyncio.run(main1())


async def main2():
    records = build_hr_policy_chunks(r"C:\Users\Dhivya\OneDrive - CONVERSE Data Solutions\Microsoft_Agent_Framework\data\HRPolicy.pdf")
    print(f'Built {len(records)} HRPolicyChunk records')

    collection = get_collection('in_memory')
    async with collection:
        await populate_collection(collection, records)
        print('Embeddings generated, collection populated')

       
        results = await collection.search('compensation and benifits', top=2)
        async for r in results.results:
            print(f'  {r.record.section_title} (page {r.record.source_page}) score={r.score:.3f}')

asyncio.run(main2())


