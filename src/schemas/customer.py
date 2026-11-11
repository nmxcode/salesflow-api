from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class CustomerBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None


class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True