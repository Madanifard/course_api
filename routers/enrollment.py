from fastapi import APIRouter, HTTPException
from typing import List

from crud.enrollment import EnrollmentRepository
from models.enrollment import EnrollmentCreate, EnrollmentResponce

router = APIRouter()
repo = EnrollmentRepository()

@router.post("/enrollments", response_model=EnrollmentResponce)
def create_enrollment(data: EnrollmentCreate):
    inserted_id = repo.create(
        enrollment_code= data.enrolle_code,
        student_code=data.student_code,
        course_code=data.course_code,
    )
    return data

@router.get("/enrollments")
def list_enrollment():
    return repo.get_all()

@router.delete("/enrollments/{code}")
def delete_enrollment(code: str):
    success = repo.delete_by_code(code)
    if not success:
        raise HTTPException(status_code=404, detail="enrollment not found")
    return {"deleted": True}

@router.get("/students/{student_code}/courses/", response_model=EnrollmentResponce) 
def get_staudent_course(student_code: str):
    course = repo.get_by_student_code(student_code)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    return course

@router.get("/courses/{course_code}/students/", response_model=EnrollmentResponce)
def get_course_students(course_code):
    course = repo.get_by_course_code(course_code)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    return course