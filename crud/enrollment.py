from typing import List, Optional
from bson import ObjectId
from database import MongoDBManager


class EnrollmentRepository:
    
    def __init__(self):
        db = MongoDBManager.get_db()
        self.collection = db["enrollments"]
    
    def create(self, enrolle_code: str, student_code: str, course_code: str):
        result = self.collection.insert_one({
            "enrolle_code": enrolle_code,
            "student_code": student_code,
            "course_code": course_code,
        })
        return str(result.inserted_id)
    
    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))
    
    def get_by_student_code(self, student_code: str):
        return self.collection.find_one({"student_code": student_code}, {"_id": 0})
    
    def get_by_course_code(self, course_code: str):
        return self.collection.find_one({"course_code": course_code}, {"_id": 0})
    
    def delete_by_code(self, enrolle_code: str) -> bool:
        result = self.collection.delete_one({"enrolle_code": enrolle_code})
        return result.deleted_count > 0
