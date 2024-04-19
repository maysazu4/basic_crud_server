from fastapi import APIRouter, HTTPException, Request
from utils.db_fns import *
from utils import auth_fns
from classes.student import *
from logger.logger import *
from utils.protect_routes import *

router = APIRouter()


@router.get("/classes/{class_name}/students")
@log
@auth_required('admin')
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
    students = load_students_db()
    students_in_class = [student for student in students if class_name in student.classes]
    logging.info('Successfully get students in class')
    return students_in_class


@router.post("/students")
@log
@auth_required('admin')
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
    students = load_students_db()
    students.append(student)
    save_student_to_db(students)
    logging.info("Student added successfully!")
    return student


@router.delete("/students")
@log
@auth_required('admin')
def delete_all_students(request: Request):
    """
    Endpoint to delete all students from the database.

    Args:
        request (Request): The HTTP request object.

    Returns:
        List: An empty list to indicate the successful deletion.

    Raises:
        HTTPException: If the user does not have sufficient privileges.
    """
    delete_all_students_from_db()
    logging.info('Successfully deleted all students')
    return []