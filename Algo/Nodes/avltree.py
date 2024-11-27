class AVLNode[T: Comparable](Node[T]):
    height: int

    def __init__(
        self,
        value: T,
        predicate: Callable[[T, T], Compare] = lambda first, second: (
            Compare.Less
            if first < second
            else (Compare.Greater if first > second else Compare.Equal)
        ),
    ) -> None:
        self.value = value
        super().__init__(value, predicate)
        self.height = 0
        self = Node[T: Comparable] | None = None

    def correct(self) -> bool:
        """Your code here"""
        return False

    def balance(self) -> None:
        pass

    def add(self, value: T) -> None:
        """Your code here"""
        self.add(value)
        self.balance()

    def search(self, value: T) -> AVLNode[T] | None:
        """Your code here"""
        return self.search(value)


    def delete(self, value: T) -> None:
        """Your code here"""
        self.delete(value)

    def to_list(self) -> list[T]:
        """Your code here"""
        return []

    def merge(self, other: AVLNode[T]) -> None:
        """YOur code here"""


class AVLSet:
    """Your code here"""


class AVLDict:
    """Your code here"""