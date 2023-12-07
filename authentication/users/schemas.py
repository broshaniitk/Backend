from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Gulshan",
                "last_name": "kumar",
                "email": "abc@gmail.com",
                "password": "Gk543211@",
            }
        }
