import re
from pypdf import PdfReader

HEADING_PATTERN=re.compile(
    r"^\s*(?:(?:SECTION|ARTICLE)\s+\d+[:.\-]?|\d+(?:\.\d+)*[\.\)]?)\s+[A-Z][A-Za-z0-9 ,'&/\-]{3,80}\s*$",
    re.MULTILINE,
)

MAX_CHUNK_CHARS=500
OVERLAP_CHARS=200


def read_pdf(pdf_path:str)->list[tuple[int,str]]:
    """Returns [(page_number, page_text), ...], 1-indexed."""
    reader=PdfReader(pdf_path)
    # print(reader.pages)[:20]
    return [(i+1,page.extract_text() or "")for i ,page in enumerate(reader.pages)]

def split_sections(pages:list[tuple[int,str]])->list[dict]:
    """Split full document into sections using heading detection.
 
    Falls back to a single 'General' section if no headings are found, so
    the pipeline never silently drops content on unusual PDF formatting.
    """
    full_text=""
    for _page_num,text in pages:
        full_text+=text+"\n"
        matches=list(HEADING_PATTERN.finditer(full_text))
        if not matches:
            return [{"heading":"General","text":full_text,"start_offset":0}]
        sections=[]
        for i, match in enumerate(matches):
            start=match.start()
            end=matches[i+1].start() if i+1<len(matches) else len(full_text)
            sections.append({
                "heading":match.group().strip(),
                "text":full_text[start:end].strip(),
                "start_offset":start,
            })
    return sections


def get_page_number(offset:int,page_offsets:list[tuple[int,int]])->int:
    page=page_offsets[0][1]
    for char_offset,page_num in page_offsets:
        if char_offset>offset:
            break
        page=page_num
    return page

def split_chunks(text:str)->list[str]:
    """Sub-chunk a section only if it exceeds the safe embedding size."""
    if len(text)<=MAX_CHUNK_CHARS:
        return[text]
    chunks,start=[],0
    while start<len(text):
        end=min(start+MAX_CHUNK_CHARS,len(text))
        chunks.append(text[start:end])
        if end==len(text):
            break
        start=end-OVERLAP_CHARS
    return chunks

def build_page_offset(pages:list[tuple[int,str]])->list[tuple[int,int]]:
    offsets=[]
    running=0
    for page_num,text in pages:
        offsets.append((running,page_num))
        running+=len(text)+1
    return offsets