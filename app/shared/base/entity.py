import uuid
from datetime import datetime


class Entity:
    """
    کلاس پایه برای موجودیت‌ها (Entities)
    """

    def __init__(self, id: str | None = None):
        self.id = id or str(uuid.uuid4())
        self.created_at = datetime.utcnow()

    def __eq__(self, other):
        return isinstance(other, Entity) and self.id == other.id

    def __repr__(self):
        return f"<Entity {self.__class__.__name__} id={self.id}>"
