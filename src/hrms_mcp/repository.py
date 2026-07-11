from sqlalchemy.orm import Session
from src.hrms_mcp.model import Employee

class EmployeeRepository:
    @staticmethod
    def get_employee_by_id(
        db:Session,
        employee_id:str
        ):
        return(
        db.query(Employee).filter(Employee.employee_id==employee_id).first()
         )
        
        
    @staticmethod
    def list_employees(db:Session):
        return db.query(Employee).all()
    
    @staticmethod
    def search_employee(db:Session,name:str):
        return (
            db.query(Employee).filter(Employee.employee_name.ilike(f"%{name}%")).all()
        )
        
    @staticmethod
    def get_department_employees(db:Session,department:str):
        return (
            db.query(Employee).filter(Employee.department.ilike(department)).all()
        )