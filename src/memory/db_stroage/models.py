from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String,Text,DateTime
from sqlalchemy.sql import func
from src.memory.db_stroage.database import engine
import asyncio

class Base(DeclarativeBase):
    pass

class ConversationHistory(Base):

    __tablename__ = "conversation_history"

    id: Mapped[int] = mapped_column(primary_key=True)

    session_id: Mapped[str] = mapped_column(
        String(100),
        index=True
    )

    role: Mapped[str] = mapped_column(String(20))

    content: Mapped[str] = mapped_column(Text)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now()
    )
    
# async def create_tables():

#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# asyncio.run(create_tables())