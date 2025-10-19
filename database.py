
from pymongo import MongoClient
from config import settings


class MongoDBManager:
    """use singleton for cooneted to mongoDB"""

    _client: MongoClient | None = None
    _db = None

    def __init__(self):
        if not MongoDBManager._client:
            MongoDBManager._client = MongoClient(
                settings.MONGO_URL,
                maxPoolSize=settings.MONGO_MAX_POOL_SIZE,
                minPoolSize=settings.MONGO_MIN_POOL_SIZE,
                connectTimeoutMS=2000,
                serverSelectionTimeoutMS=2000,
            )
            MongoDBManager._db = MongoDBManager._client[settings.MONGO_DB_NAME]

    @classmethod
    def get_db(cls):
        """return instance of db"""
        if cls._db is None:
            cls()
        return cls._db

    @classmethod
    def close(cls):
        if cls._client:
            cls._client.close()
            cls._client = None
            cls._db = None

    @classmethod
    def setup(cls):
        """Create Collection Automatic"""
        db = cls.get_db()
        
        collections = ["instructors", "enrollments", "students", "courses"]
        for item in collections:
            if item not in db.list_collection_names():
                db.create_collection(item)
                print(f"🆕 Created collection: {item}")
                
        print("⚙️ MongoDB initialized and indexes created.")