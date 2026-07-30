from collections.abc import Sequence
from typing import Any
from agent_framework import HistoryProvider,Message

class PostgreHistoryProvider(HistoryProvider):
    def __init__(self,db):
        super().__init__(
        source_id="postgres-history",
        load_messages=True,
        )
        self.db=db
    async def get_messages(self,session_id:str|None,**kwargs:Any,)->list[Message]:
        rows=await self.db.load_messages(session_id)
        history=[]
        for row in rows:
            history.append(
                Message(
                    role=row.role,
                    contents=row.content,
                )
            )
        return history
    async def save_messages(self,session_id:str|None,messages:Sequence[Message],**kwargs:Any,):
        await self.db.save_messages(
            session_id,messages
        )