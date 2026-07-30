from sqlalchemy import select
from src.memory.db_stroage.database import SessionLocal
from src.memory.db_stroage.models import ConversationHistory

class ConversationDB:
    async def load_messages(self,session_id):
        async with SessionLocal() as session:
            query=(select(ConversationHistory).where(ConversationHistory.session_id==session_id).order_by(ConversationHistory.id))
            result=await session.execute(query)
            return result.scalars().all()
    async def save_messages(self,session_id,messages):
        async with SessionLocal() as session:
           for message in messages:
                text = ""

                for item in message.contents:
                    if item.type == "text":
                        text += item.text

                session.add(
                    ConversationHistory(
                        session_id=session_id,
                        role=message.role,
                        content=text
                    )
                )
               
           await session.commit()
            
            