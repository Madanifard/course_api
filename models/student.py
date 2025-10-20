from pydantic import BaseModel, Field
from typing import Optional


class StudentCreate(BaseModel):
    name: str = Field(..., example="Amir")
    family: str = Field(..., example="Moradi")
    username: str = Field(..., example="Amir3456")
    student_code: str = Field(..., example="GHJ908")


class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Amir")
    family: Optional[str] = Field(None, example="Moradi")
    username: Optional[str] = Field(None, example="Amir3456")
    student_code: Optional[str] = Field(None, example="GHJ908")


class StudentResponse(BaseModel):
    name: str = Field(..., example="Amir")
    family: str = Field(..., example="Moradi")
    username: str = Field(..., example="Amir3456")
    student_code: str = Field(..., example="INST001")
