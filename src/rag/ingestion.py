from semantic_kernel.connectors.azure_ai_search import AzureAISearchCollection
from semantic_kernel.connectors.in_memory import InMemoryCollection
from src.rag.chunking import *
from src.rag.model import HRPolicyChunk

def build_hr_policy_chunks(pdf_path:str,document_name:str="HR Policy Handbook")->list[HRPolicyChunk]:
    """Extract, section-split, and size-chunk a PDF into HRPolicyChunk records."""
    pages=read_pdf(pdf_path)
    page_offset=build_page_offset(pages)
    sections=split_sections(pages)
    records:list[HRPolicyChunk]=[]
    for section in sections:
        for sub_text in split_chunks(section["text"]):
            stripped=sub_text.strip()
            if not stripped:
                continue
            records.append(
                HRPolicyChunk(
                    section_title=section["heading"],
                    content=stripped,
                    source_page=get_page_number(section["start_offset"],page_offset),
                    document_name=document_name,
                )
            )
    return records

def get_collection(backend:str):
    if backend == "in_memory":
        return InMemoryCollection(record_type=HRPolicyChunk,collection_name="hr-policy")
    if backend=="azure_search":
        return AzureAISearchCollection[str,HRPolicyChunk](
            record_type=HRPolicyChunk,
            collection_name="hr-policy",
        )
    raise ValueError(f"Unknown backend:{backend}. Use 'in_memory' or 'azure_search'")

async def populate_collection(collection,records:list[HRPolicyChunk])->None:
    await collection.ensure_collection_exists()
    await collection.upsert(records)


async def ingest_hr_policy(pdf_path:str,backend:str,document_name:str="HR Policy Handbook")->int:
    records=build_hr_policy_chunks(pdf_path,document_name)
    collection=get_collection(backend)
    async with collection:
        await populate_collection(collection,records)
    return len(records)