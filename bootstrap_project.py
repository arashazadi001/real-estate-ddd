import os

def create_file(path, content=""):
    directory = os.path.dirname(path)

    if directory:  # فقط اگر مسیر وجود داشت فولدر بساز
        os.makedirs(directory, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())

    print(f"✅ Created: {path}")

# 1. Structure Definitions
FOLDERS = [
    "app/domain/entities", "app/domain/aggregates", "app/domain/value_objects",
    "app/domain/rules", "app/domain/policies", "app/domain/events",
    "app/domain/exceptions", "app/domain/enums",
    "app/application/mediator", "app/application/commands", "app/application/queries",
    "app/application/handlers", "app/application/dto", "app/application/interfaces",
    "app/application/behaviors",
    "app/infrastructure/persistence/models", "app/infrastructure/persistence/migrations",
    "app/infrastructure/repositories", "app/infrastructure/auth", "app/infrastructure/cache",
    "app/presentation/api/routes", "app/presentation/api/dependencies",
    "app/presentation/schemas",
    "app/shared/result", "app/shared/base", "app/shared/utils",
    "tests"
]

# 2. Content for Foundation Files
RESULT_PY = """
from typing import Generic, TypeVar, Optional, Any

T = TypeVar("T")

class Result(Generic[T]):
    def __init__(self, is_success: bool, value: Optional[T] = None, error: Optional[str] = None):
        self.is_success = is_success
        self.value = value
        self.error = error

    @staticmethod
    def success(value: T = None) -> "Result[T]":
        return Result(True, value=value)

    @staticmethod
    def failure(error: str) -> "Result[T]":
        return Result(False, error=error)

    def __repr__(self):
        return f"Success({self.value})" if self.is_success else f"Failure({self.error})"
"""

BASE_ENTITY_PY = """
import uuid
from datetime import datetime

class Entity:
    def __init__(self, id: uuid.UUID = None):
        self.id = id or uuid.uuid4()
        self.created_at = datetime.utcnow()

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
"""

VALUE_OBJECT_PY = """
from dataclasses import dataclass

@dataclass(frozen=True)
class ValueObject:
    \"\"\"Base class for Value Objects (Immutable)\"\"\"
    pass
"""

DOMAIN_EXCEPTION_PY = """
class DomainException(Exception):
    \"\"\"Base class for all domain exceptions\"\"\"
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
"""

REQUIREMENTS_TXT = """
fastapi==0.110.0
uvicorn==0.27.1
pydantic==2.6.3
pydantic-settings==2.2.1
sqlalchemy==2.0.27
alembic==1.13.1
asyncpg==0.29.0
python-multipart==0.0.9
"""

MAIN_PY = """
from fastapi import FastAPI

app = FastAPI(title="Real Estate Clean Architecture")

@app.get("/")
async def root():
    return {"message": "Welcome to Real Estate API"}
"""

# 3. Execution
def bootstrap():
    print("🚀 Starting Project Bootstrap...")
    
    # Create Folders and __init__.py
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)
        create_file(os.path.join(folder, "__init__.py"), "")
    
    # Create Foundation Files
    create_file("app/shared/result/result.py", RESULT_PY)
    create_file("app/shared/base/entity.py", BASE_ENTITY_PY)
    create_file("app/shared/base/value_object.py", VALUE_OBJECT_PY)
    create_file("app/domain/exceptions/base_exception.py", DOMAIN_EXCEPTION_PY)
    create_file("requirements.txt", REQUIREMENTS_TXT)
    create_file("main.py", MAIN_PY)
    
    print("\\n✨ Bootstrap Finished! Project is ready for development.")

if __name__ == "__main__":
    bootstrap()
