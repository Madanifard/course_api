# models/course.py
from pydantic import BaseModel, Field
from typing import Optional


class CourseCreate(BaseModel):
    name: str = Field(..., example="Ali")
    family: str = Field(..., example="Ahmadi")
    username: str = Field(..., example="ali123")
    course_code: str = Field(..., example="XVB4356")
    instructor_code: str = Field(..., example="INST001")


class CourseUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Ali")
    family: Optional[str] = Field(None, example="Ahmadi")
    username: Optional[str] = Field(None, example="ali123")
    course_code: Optional[str] = Field(None, example="XVB4356")
    instructor_code: Optional[str] = Field(None, example="INST001")


class CourseResponse(BaseModel):
    name: str = Field(..., example="Ali")
    family: str = Field(..., example="Ahmadi")
    username: str = Field(..., example="ali123")
    course_code: str = Field(..., example="XVB4356")
    instructor_code: str = Field(..., example="INST001")
