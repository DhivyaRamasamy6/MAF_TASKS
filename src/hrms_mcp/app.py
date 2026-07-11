from mcp.server.fastmcp import FastMCP
from src.hrms_mcp.repository import EmployeeRepository
from src.hrms_mcp.database import SessionLocal

mcp=FastMCP("HRMS mcp server")
@mcp.tool(description="Retrieve employee details by employee ID")
def get_employee(employee_id:str)->dict:
    """Retrieve employee details by employee ID"""
   
    db=SessionLocal()
    try:
        employee=EmployeeRepository.get_employee_by_id(
            db,
            employee_id
        )
        if employee is None:
            return {
                "status":"error",
                "message":"Employee not found"
            }
        return{
            "employee_id":employee.employee_id,
            "employe_name":employee.employee_name,
            "department":employee.department,
            "designation":employee.designation,
            "email":employee.email
        }
    finally:
        db.close()
        
        
        
@mcp.tool(description="Retrive all the employees from the employees table")
def list_employees():
    db=SessionLocal()
    try:
        employees=EmployeeRepository.list_employees(db)
        return[
            {
            "employee_id":employee.employee_id,
            "employe_name":employee.employee_name,
            "department":employee.department,
            "designation":employee.designation,
            "email":employee.email
            
            }
               for employee in employees
            ]
    finally:
        db.close()
        

@mcp.tool(description="Search employees by employee name.")
def searh_employee(name:str)->dict:
    """Retrieve employee details by employee ID"""
   
    db=SessionLocal()
    try:
        employees=EmployeeRepository.search_employee(
            db,
            name
        )
       
        return[
            {
            "employee_id":employee.employee_id,
            "employe_name":employee.employee_name,
            "department":employee.department,
            "designation":employee.designation,
            "email":employee.email
               }
               for employee in employees
               ]
    finally:
        db.close()

        
@mcp.tool(description="Retrieve all employees belonging to a department.")
def get_department_employees(department:str):
    db=SessionLocal()
    try:
        employees=EmployeeRepository.get_department_employees(
            db,
            department
        )
    
        return[
            {
            "employee_id":employee.employee_id,
            "employe_name":employee.employee_name,
            "department":employee.department,
            "designation":employee.designation,
            "email":employee.email
            }
            for employee in employees
            ]
    finally:
        db.close()

if __name__=="__main__":
    mcp.run()