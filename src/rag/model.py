from dataclasses import dataclass,field
from typing import Annotated
from uuid import uuid4
from src.config.settings import embedding_generator
from semantic_kernel.data.vector import VectorStoreField,vectorstoremodel
from semantic_kernel.data.vector import DistanceFunction
import os
from dotenv import load_dotenv
load_dotenv()
@vectorstoremodel
@dataclass
class HRPolicyChunk:
    chunk_id:Annotated[str,VectorStoreField("key")]=field(default_factory=lambda:str(uuid4()))
    section_title:Annotated[str,VectorStoreField("data",is_indexed=True)]=""
    content:Annotated[str,VectorStoreField("data",is_full_text_indexed=True)]=""
    source_page:Annotated[int,VectorStoreField("data",is_indexed=True)]=0
    document_name:Annotated[str,VectorStoreField("data",is_indexed=True)]=""
    vector:Annotated[list[float]|str|None,VectorStoreField("vector",dimensions=1536,distance_function=DistanceFunction.COSINE_SIMILARITY,embedding_generator=embedding_generator)]=None
    
    def __post_init__(self)->None:
        if self.vector is None:
            self.vector=f"{self.section_title}. {self.content}"
