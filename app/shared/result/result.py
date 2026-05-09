from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class Result(Generic[T]):
    """
    Result pattern برای هندل منظم موفقیت یا شکست عملیات
    """

    def __init__(self, is_success: bool, value: Optional[T] = None, error: Optional[str] = None):
        if is_success and error is not None:
            raise ValueError("موفقیت نمی‌تواند خطا داشته باشد.")
        if not is_success and error is None:
            raise ValueError("خطا باید پیام خطا داشته باشد.")

        self.is_success = is_success
        self.is_failure = not is_success
        self.value = value
        self.error = error

    @classmethod
    def success(cls, value: Optional[T] = None) -> "Result[T]":
        return cls(True, value=value)

    @classmethod
    def failure(cls, error: str) -> "Result[T]":
        return cls(False, error=error)

    def __repr__(self) -> str:
        if self.is_success:
            return f"Result(success, value={self.value})"
        return f"Result(failure, error='{self.error}')"
