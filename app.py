from fastapi import FastAPI
from routes import student
from routes import auth_router

app = FastAPI()

# routes
app.include_router(student.router)
app.include_router(auth_router.router)


