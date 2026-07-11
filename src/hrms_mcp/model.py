from sqlalchemy import Column,String,Date,Numeric,TIMESTAMP,text
from sqlalchemy.orm import DeclarativeBase
from src.hrms_mcp.database import engine
class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__="employees"
    employee_id=Column(String(20),primary_key=True)
    employee_name=Column(String(100),nullable=False)
    department=Column(String(100),nullable=False)
    designation=Column(String(100),nullable=False)
    email=Column(String(150),unique=True,nullable=False)
     
# Base.metadata.create_all(bind=engine)

# print("Tables created successfully.")