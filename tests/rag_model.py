from src.rag.model import HRPolicyChunk

CHUNK=HRPolicyChunk(section_title='Test',content="Some policy text",source_page=1)
print(CHUNK)
print("vector field: ",CHUNK.vector)

# HRPolicyChunk(chunk_id='38be3d23-c3bf-49a1-962c-3967af61f611', section_title='Test', content='Some policy text', source_page=1, document_name='', vector='Test. Some policy text')
# vector field:  Test. Some policy text