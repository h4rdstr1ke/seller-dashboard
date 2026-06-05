from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class SellerCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    middle_name: Optional[str] = None
    company_name: str
    inn: str = Field(min_length=10, max_length=12)
    phone: Optional[str] = None

class SellerResponse(BaseModel):
    id: str
    email: EmailStr
    first_name: str
    last_name: str
    company_name: str
    inn: str

    class Config:
        from_attributes = True  