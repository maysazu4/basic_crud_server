from fastapi import APIRouter, HTTPException, Request
from utils.db_fns import *
from utils import auth_fns
from classes.student import *

router = APIRouter()

@router.get("/students")
async def read_students(request: Request):
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

@router.get("/classes/{class_name}/students")
def get_students_in_class(class_name: str, request: Request):
    """
    Endpoint to retrieve students in a specific class.

    Args:
        class_name (str): The name of the class to retrieve students for.
        request (Request): The HTTP request object.

    Returns:
        List[Student]: A list of students in the specified class.

    Raises:
        HTTPException: If the user does not have sufficient privileges or no token is provided.
    """
    user_role = auth_fns.check_token(request)
    if user_role == "admin":
        students = load_students_db()
        students_in_class = [student for student in students if class_name in student.classes]
        return students_in_class
    elif user_role == 'guest':
        raise HTTPException(status_code=403, detail="Access denied")
    else:
        raise HTTPException(400, "no token")

@router.post("/students")
def add_student(student: Student, request: Request):
    """
    Endpoint to add a new student.

    Args:
        student (Student): The student object to be added.
        request (Request): The HTTP request object.

    Returns:
        Student: The added student.

    Raises:
        HTTPException: If the user does not have sufficient privileges or no token is provided.
    """
    user_role = auth_fns.check_token(request)
    if user_role == "admin":
        students = load_students_db()
        students.append(student)
        save_student_to_db(students)
        return student
    elif user_role == 'guest':
        raise HTTPException(status_code=403, detail="Access denied")
    else:
        raise HTTPException(400, "no token")
