from typing import List, Optional
from bson import ObjectId
from database import MongoDBManager


class CourseRepository:

    def __init__(self):
        db = MongoDBManager.get_db()
        self.collection = db["courses"]

    def create(self, name: str, family: str, username: str, course_code: str, instructor_code: str) -> str:
        result = self.collection.insert_one({
            "name": name,
            "family": family,
            "username": username,
            "course_code": course_code,
            "instructor_code": instructor_code,
        })
        return str(result.inserted_id)

    def get_all(self) -> List[dict]:
        return list(self.collection.find({}, {"_id": 0}))

    def get_by_code(self, course_code: str) -> Optional[dict]:
        return self.collection.find_one({"course_code": course_code}, {"_id": 0})

    def update_by_code(self, course_code: str, data: dict) -> bool:
        result = self.collection.update_one(
            {"course_code": course_code},
            {"$set": data}
        )
        return result.modified_count > 0

    def delete_by_code(self, course_code: str) -> bool:
        #TODO: delete other enrollment
        result = self.collection.delete_one({"course_code": course_code})
        return result.deleted_count > 0
