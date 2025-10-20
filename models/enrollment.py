from pydantic import BaseModel, Field
from typing import Optional

class EnrollmentCreate(BaseModel):
    student_code: str = Field(..., example="GHJ908")
    course_code: str = Field(..., example="XVB4356")
    enrolle_code: str = Field(..., example="UFP20948")
    
class EnrollmentResponce(BaseModel):
    student_code: str = Field(..., example="GHJ908")
    course_code: str = Field(..., example="XVB4356")
    enrolle_code: str = Field(..., example="UFP20948")