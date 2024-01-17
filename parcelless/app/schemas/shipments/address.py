from pydantic import BaseModel, EmailStr, Field


class Address(BaseModel):
    address1: str = Field(max_length=75)
    address2: str | None = None
    name: str
    company: str | None = None
    postalcode: str = Field(max_length=10)
    city: str
    country: str = Field(max_length=2)
    email: EmailStr
    phone: str | None = Field(default=None, max_length=15)
