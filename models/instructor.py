from pydantic import BaseModel, Field

class InstructorBase(BaseModel):
    name: str = Field(..., example="Ali")
    family: str = Field(..., example="Ahmadi")
    username: str = Field(..., example="ali.ahmadi")
    instructor_code: str = Field(..., example="INS12345")

class InstructorCreate(InstructorBase):
    pass

class InstructorUpdate(BaseModel):
    name: str | None = None
    family: str | None = None
    username: str | None = None

class InstructorResponse(InstructorBase):
    class Config:
        orm_mode = True
