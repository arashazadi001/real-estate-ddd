from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Type, Any, Callable, Awaitable
from app.shared.result.result import Result

TResponse = TypeVar("TResponse")
TRequest = TypeVar("TRequest")

class IRequest(Generic[TResponse], ABC):
    pass

class IRequestHandler(Generic[TRequest, TResponse], ABC):
    @abstractmethod
    async def handle(self, request: TRequest) -> Result[TResponse]:
        pass

# --- بخش جدید ---
class IPipelineBehavior(ABC):
    """اینترفیس برای رفتارهای میانی (Middlewares) در مدیتور"""
    @abstractmethod
    async def handle(self, request: Any, next_call: Callable[[], Awaitable[Result[Any]]]) -> Result[Any]:
        pass
