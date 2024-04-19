from fastapi import APIRouter, HTTPException, Request
from utils.db_fns import *
from utils import auth_fns
from classes.student import *
from logger.logger import *
from utils.protect_routes import *
router = APIRouter()

@router.get("/students")
@log
def read_students(request: Request):
    """
    Endpoint to retrieve all students.

    Args:
        request (Request): The HTTP request object.

    Returns:
        List[Student]: A list of all students.
    """
    if auth_fns.check_token(request):
        school_json = load_students_db()
        return school_json
    else:
        raise HTTPException(400, "no token")

@router.get("/students/{student_id}")
@log
def get_student(student_id: int, request: Request):
    """
    Endpoint to retrieve a specific student by ID.

    Args:
        student_id (int): The ID of the student to retrieve.
        request (Request): The HTTP request object.

    Returns:
        Student: The student with the specified ID.

    Raises:
        HTTPException: If the specified student ID is not found.
    """
    if auth_fns.check_token(request):
        students = load_students_db()
        for student in students:
            if student.id == student_id:
                return student
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        raise HTTPException(400, "no token")


   

@router.delete("/students/{student_id}")
@log
def delete_student(student_id: int, request: Request):
    """
    Endpoint to delete a specific student by ID.

    Args:
        student_id (int): The ID of the student to delete.
        request (Request): The HTTP request object.

    Returns:
        str: A message indicating the successful deletion.

    Raises:
        HTTPException: If the specified student ID is not found or if authentication fails.
    """
    if auth_fns.check_token(request):
        students = load_students_db()
        for student in students:
            if student.id == student_id:
                students.remove(student)
                save_student_to_db(students)
                return 'Successfully deleted'
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        raise HTTPException(400, "No token provided")
