import bcrypt
import utils.db_fns as fns
import jwt
from base64 import b64decode as decode

def hash_password(password: str) -> str:
    """
    Hashes the given password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(stored_pass, user_pass):
    """
    Verifies whether a given password matches a stored hashed password.

    Args:
        stored_pass (str): The stored hashed password.
        user_pass (str): The password to verify.

    Returns:
        bool: True if the password matches the stored hashed password, False otherwise.
    """
    return bcrypt.checkpw(user_pass.encode('utf-8'), stored_pass.encode('utf-8'))

def prepare_new_user_data(password, username, role):
    """
    Prepares new user data by hashing the password and adding it to the database.

    Args:
        password (str): The user's password.
        username (str): The username.
        role (str): The user's role.

    Returns:
        dict: The updated user data.
    """
    hashed_password = hash_password(password)
    current_db = fns.load_auth_db()
    current_db[username] = {
        "username": username,
        "password": hashed_password,
        "role": role
    }
    return current_db

def generate_jwt(payload):
    """
    Generates a JSON Web Token (JWT) using the provided payload.

    Args:
        payload (dict): The data to include in the JWT payload.

    Returns:
        str: The encoded JWT.
    """
    SECRET_KEY = "your-secret-key"
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")   
    print('encoded_jwt: ', encoded_jwt)
    return encoded_jwt

def verify_jwt(user_jwt):
    """
    Verifies a JSON Web Token (JWT) and retrieves the user's role.

    Args:
        user_jwt (str): The JWT token to verify.

    Returns:
        str: The user's role if the token is valid, False otherwise.
    """
    try:
        SECRET_KEY = "your-secret-key"
        data = jwt.decode(user_jwt, SECRET_KEY, algorithms="HS256")
        return data["user role"]
    except Exception as e:
        print('e: ', e)
        print("bad token")
        return False

def check_token(request):
    """
    Checks for a JWT token in the authorization header of an HTTP request.

    Args:
        request: The HTTP request object.

    Returns:
        str: The user's role if the token is valid, None otherwise.
    """
    auth_header = request.headers.get('authorization')
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        try:
            user_role = verify_jwt(token)
            if user_role:
                return user_role
        except Exception as e:
            raise e
    return None
