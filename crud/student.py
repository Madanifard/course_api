from typing import List, Optional
from bson import ObjectId
from database import MongoDBManager


class StudentRepository:

    def __init__(self):
        db = MongoDBManager.get_db()
        self.collection = db["students"]

    def create(self, name: str, family: str, username: str, student_code: str) -> str:
        result = self.collection.insert_one({
            "name": name,
            "family": family,
            "username": username,
            "student_code": student_code,
        })
        return str(result.inserted_id)

    def get_all(self) -> List[dict]:
        return list(self.collection.find({}, {"_id": 0}))

    def get_by_code(self, student_code: str) -> Optional[dict]:
        return self.collection.find_one({"student_code": student_code}, {"_id": 0})

    def update_by_code(self, student_code: str, data: dict) -> bool:
        result = self.collection.update_one(
            {"student_code": student_code},
            {"$set": data}
        )
        return result.modified_count > 0

    def delete_by_code(self, student_code: str) -> bool:
        result = self.collection.delete_one({"student_code": student_code})
        return result.deleted_count > 0
