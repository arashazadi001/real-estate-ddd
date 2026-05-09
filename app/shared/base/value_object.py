from dataclasses import dataclass

@dataclass(frozen=True)
class ValueObject:
    """
    کلاس پایه برای Value Objectها
    تغییرناپذیر و مقایسه بر اساس مقدار (Equality by Value)
    """

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
