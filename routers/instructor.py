from fastapi import APIRouter, HTTPException
from typing import List

from crud.instructor import InstructorsRepository
from models.instructor import InstructorCreate, InstructorUpdate, InstructorResponse

router = APIRouter()
repo = InstructorsRepository()


@router.post("/instructors", response_model=InstructorResponse)
def create_instructor(data: InstructorCreate):
    inserted_id = repo.create(
        name=data.name,
        family=data.family,
        username=data.username,
        instructor_code=data.instructor_code
    )
    return data


@router.get("/instructors", response_model=List[InstructorResponse])
def list_instructors():
    return repo.get_all()


@router.get("/instructors/{code}", response_model=InstructorResponse)
def get_instructor(code: str):
    instructor = repo.get_by_code(code)
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor


@router.put("/instructors/{code}", response_model=InstructorResponse)
def update_instructor(code: str, data: InstructorUpdate):
    success = repo.update_by_code(code, data.dict(exclude_unset=True))
    if not success:
        raise HTTPException(status_code=404, detail="Instructor not found or not updated")
    instructor = repo.get_by_code(code)
    return instructor


@router.delete("/instructors/{code}")
def delete_instructor(code: str):
    success = repo.delete_by_code(code)
    if not success:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return {"deleted": True}
