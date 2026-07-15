from src.rag.chunking import read_pdf,split_chunks,split_sections,build_page_offset,get_page_number

pages=read_pdf(r"C:\Users\Dhivya\OneDrive - CONVERSE Data Solutions\Microsoft_Agent_Framework\data\HRPolicy.pdf")
print(f"Extracted pages {len(pages)} pages")
offsets=build_page_offset(pages)
sections=split_sections(pages)
print(f"Found {len(sections)} sections")
for s in sections:
    for chunk_text in split_chunks(s['text']):
        page = get_page_number(s['start_offset'], offsets)
        print(f"{s["heading"]} page {page}: {chunk_text[:50]!r}...")