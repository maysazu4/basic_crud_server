from fastapi import FastAPI
from routes import student_router
from routes import auth_router
from routes import admin_router
from routes import chat_router
from routes import image_router
app = FastAPI()

# routes
app.include_router(student_router.router)
app.include_router(admin_router.router)
app.include_router(auth_router.router)
app.include_router(image_router.router)
app.include_router(chat_router.router)


