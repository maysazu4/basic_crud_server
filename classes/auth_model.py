from pydantic import BaseModel,Field

class Auth_Model(BaseModel):
    username: str
    password: str
    role: str = Field(default="guest")
