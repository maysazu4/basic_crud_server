import logging
from functools import wraps
logging.basicConfig(filename='logger\logging.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            logging.error("An error occurred: %s", e)
            return e
    return wrapper