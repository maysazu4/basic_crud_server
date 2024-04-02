from fastapi import APIRouter
import utils.auth_fns as auth_fns
import utils.db_fns as db_fns
from classes.auth_model import Auth_Model

router = APIRouter()

@router.post('/auth/sign_up')
def sign_up(body:Auth_Model):
    """
    Endpoint for user sign-up.

    Registers a new user by adding their credentials to the authentication database.

    Args:
        body (Auth_Model): The request body containing user credentials (username, password, and role).

    Returns:
        dict: A dictionary containing a message confirming user creation and an authentication token.
    """
    updated_db = auth_fns.prepare_new_user_data(body.password,body.username,body.role)
    db_fns.save_user_to_db(updated_db)
    auth_token = auth_fns.generate_jwt({"user role":body.role})
    return {"msg":"user created","token":auth_token}
    

@router.post('/auth/sign_in')
def sign_in(body:Auth_Model):
    """
    Endpoint for user sign-in.

    Authenticates a user based on provided credentials (username and password).

    Args:
        body (Auth_Model): The request body containing user credentials (username and password).

    Returns:
        dict: A dictionary containing a message indicating sign-in success or failure, along with an authentication token.
    """
    try:
        stored_user = db_fns.find_user_in_db(body.username)
        if stored_user:
            stored_pass = stored_user["password"]
            role = stored_user["role"]
            if auth_fns.verify_password(stored_pass,body.password):
                auth_token = auth_fns.generate_jwt({"user role":role})
                return {"msg":"user sign in successfully","token":auth_token}
            else:
                return {"msg":"invalid credentials"}
    except Exception as e:
        print(e)
        return {"msg": "no such username"}
