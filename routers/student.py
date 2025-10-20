from fastapi import APIRouter, HTTPException
from typing import List

from crud.student import StudentRepository
from models.student import StudentCreate, StudentUpdate, StudentResponse

router = APIRouter()
repo = StudentRepository()


@router.post("/student", response_model=StudentResponse)
def create_student(data: StudentCreate):
    inserted_id = repo.create(
        name=data.name,
        family=data.family,
        username=data.username,
        student_code=data.student_code,
    )
    return data


@router.get("/students", response_model=List[StudentResponse])
def list_students():
    return repo.get_all()


@router.get("/student/{code}", response_model=StudentResponse)
def get_student(code: str):
    student = repo.get_by_code(code)
    if not student:
        raise HTTPException(status_code=404, detail="student not found")
    return student


@router.put("/students/{code}", response_model=StudentResponse)
def update_student(code: str, data: StudentUpdate):
    success = repo.update_by_code(code, data.dict(exclude_unset=True))
    if not success:
        raise HTTPException(
            status_code=404, detail="student not found or not updated")
    student = repo.get_by_code(code)
    return student


@router.delete("/students/{code}")
def delete_student(code: str):
    success = repo.delete_by_code(code)
    if not success:
        raise HTTPException(status_code=404, detail="student not found")
    return {"deleted": True}
