from fastapi import APIRouter, HTTPException
from typing import List

from crud.course import CourseRepository
from models.course import CourseUpdate, CourseCreate, CourseResponse

router = APIRouter()
repo = CourseRepository()


@router.post("/course", response_model=CourseResponse)
def create_course(data: CourseCreate):
    inserted_id = repo.create(
        name=data.name,
        family=data.family,
        username=data.username,
        course_code=data.course_code,
        instructor_code=data.instructor_code
    )
    return data


@router.get("/courses", response_model=List[CourseResponse])
def list_courses():
    return repo.get_all()


@router.get("/course/{code}", response_model=CourseResponse)
def get_course(code: str):
    course = repo.get_by_code(code)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    return course


@router.put("/courses/{code}", response_model=CourseResponse)
def update_course(code: str, data: CourseUpdate):
    success = repo.update_by_code(code, data.dict(exclude_unset=True))
    if not success:
        raise HTTPException(status_code=404, detail="course not found or not updated")
    course = repo.get_by_code(code)
    return course


@router.delete("/courses/{code}")
def delete_course(code: str):
    success = repo.delete_by_code(code)
    if not success:
        raise HTTPException(status_code=404, detail="course not found")
    return {"deleted": True}
