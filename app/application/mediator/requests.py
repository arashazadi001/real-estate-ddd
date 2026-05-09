from typing import Generic, TypeVar

TResponse = TypeVar("TResponse")


class Command(Generic[TResponse]):
    pass


class Query(Generic[TResponse]):
    pass
