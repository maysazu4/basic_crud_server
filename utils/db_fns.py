from classes.student import Student
from typing import List
import json
import os

Students_db = "data_base/students.json"
Auth_db = 'data_base/auth_db.json' 

def load_file(filename):
    """
    Loads data from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict or None: The loaded data as a dictionary, or None if the file is empty or not found.
    """
    try:
        with open(filename, "r") as file:
            if os.path.getsize(filename) == 0:
                return None
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None
        
def load_students_db() -> List[Student]:
    """
    Loads student data from the students database file.

    Returns:
        List[Student]: A list of Student objects loaded from the database.
    """
    data = load_file(Students_db)
    if data is None:
        return []
    return [Student(**student_data) for student_data in data]
   
def save_student_to_db(students: List[Student]): 
    """
    Saves student data to the students database file.

    Args:
        students (List[Student]): A list of Student objects to be saved to the database.
    """
    with open(Students_db, "w") as file:
        json.dump([student.model_dump() for student in students], file, indent=3)
        
def load_auth_db(db=Auth_db):
    """
    Loads authentication data from the authentication database file.

    Args:
        db (str): The path to the authentication database file.

    Returns:
        dict: A dictionary containing the loaded authentication data.
    """
    data = load_file(db)
    if data is None:
        return {}
    return data
        
def save_user_to_db(updated_db):
    """
    Saves user data to the authentication database file.

    Args:
        updated_db (dict): The updated user data to be saved to the database.
    """
    with open(Auth_db, 'w') as f:
        json.dump(updated_db, f, indent=3)
        
def find_user_in_db(username):
    """
    Finds a user in the authentication database by username.

    Args:
        username (str): The username of the user to search for.

    Returns:
        dict: The user data if found.

    Raises:
        FileNotFoundError: If the specified username is not found in the database.
    """
    db = load_auth_db(Auth_db)
    if username in db:
        return db[username]
    else:
        raise FileNotFoundError(f'Username: {username} not found in the database.')
