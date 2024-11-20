from __future__ import annotations
from abc import ABCMeta, abstractmethod
from enum import Enum, auto
from typing import Any, Callable, Iterable


class Compare(Enum):
    Less = auto()
    Equal = auto()
    Greater = auto()


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...

    @abstractmethod
    def __gt__(self, other: Any) -> bool: ...

    @abstractmethod
    def __eq__(self, other: Any) -> bool: ...


class Node[T: Comparable]:
    value: T
    left: Node[T] | None
    right: Node[T] | None
    parent: Node[T] | None
    predicate: Callable[[T, T], Compare]

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
        self.predicate = predicate
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self, level=0) -> str:
        result = " " * (level * 4) + '|' + str(self.value) + "\n"
        if self.left:
            result += 'l' + self.left.__str__(level + 1)
        if self.right:
            result += 'r' + self.right.__str__(level + 1)
        return result

    def __repr__(self):
        return "<tree node representation>"

    def correct(self) -> bool:
        if self.left is not None:
            if not self.left.correct():
                return False
            if not self.predicate(self.left.value, self.value) == Compare.Less:
                return False
        if self.right is not None:
            if not self.right.correct():
                return False
            if not self.predicate(self.right.value, self.value) == Compare.Greater:
                return False
        return True

    def add(self, value: T) -> None:
        if self.predicate(value, self.value) == Compare.Less:
            if self.left is None:
                self.left = Node(value, self.predicate)
                self.left.parent = self  
            else:
                self.left.add(value)
        elif self.predicate(value, self.value) == Compare.Greater:
            if self.right is None:
                self.right = Node(value, self.predicate)
                self.right.parent = self 
            else:
                self.right.add(value)

    def search(self, value: T) -> Node[T] | None: 
        if self.value == value: 
            return self
        if self.predicate(value, self.value) == Compare.Less: 
            if self.left is None:
                return None
            return self.left.search(value) 
        if self.predicate(value, self.value) == Compare.Greater: 
            if self.right is None:
                return None
            return self.right.search(value) 

    def delete(self, value: T) -> None:
        if self.predicate(value, self.value) == Compare.Less:
            if self.left is not None:
                self.left.delete(value)
        elif self.predicate(value, self.value) == Compare.Greater:
            if self.right is not None:
                self.right.delete(value)
        else:
            if self.left is None or self.right is None:
                self.__change_parent(self.left or self.right)
            else:
                min_node = self.right._find_min()
                self.value = min_node.value
                min_node.delete(min_node.value)

    def __change_parent(self, new_node: Node[T] | None) -> None:
        if self.parent:
            if self.parent.left == self:
                self.parent.left = new_node
            else:
                self.parent.right = new_node

    def to_list(self) -> list[T]:
        values = []
        if self.left is not None: 
            values.extend(self.left.to_list() )
        values.append(self.value) 
        if self.right is not None: 
            values.extend(self.right.to_list())
        return values

    def merge(self, other: Node[T]) -> None:
        other_elems = other.to_list()
        self_elems = self.to_list()
        self_elems.extend(other_elems)
        elems = sorted(self_elems)
        print(elems)
        self.value = elems[0]
        for i in range(len(elems)):
            self.add(elems[i])


class MySet[collection: Iterable[T]]:

    def __init__(self, collection: Iterable[T]):
        self.node: Node[T: Comparable] | None = None
        for val in collection:
            self.add(val)

    def add(self, value: T):
        if self.node is None:
            self.node = Node(value)
        else:
            self.node.add(value)
    
    def __str__(self) -> str:
        vals = self.node.to_list()
        return f"{{{", ".join(map(str, vals))}}}"
    
    def str_node(self):
        return self.node.__str__()

    def delete(self, value):
        self.node.delete(value)
    
    def intersection(self, other):
        inter = MySet([])
        for i in self.node.to_list():
            if other.node.search():
                inter.add(i)
        return inter
    
    def union(self, other):
        return MySet(self.node.merge(other.node).to_list())
    
    & = intersection
    | = union

    def is_subset(self, other):
        self_vals = self.node.to_list()
        other_vals = other.node.to_list()

        for i in other_vals:
            if i not in self_vals:
                return False
        return True

        
    def is_empty():
        pass  
    def __in__():
        pass

root = MySet(collection=[1,2,3,4])
root.add(5)
root.add(15)
root.add(7)

# root2 = Set[int](value=13)
# root2.add(382)
# root2.add(1)
# root2.add(12)
# root2.add(33)
# root.merge(root2)
# print(root)

# root3 = Node[int](value=8)
# root3.add(10)
# root3.add(109)
# root3.add(17)

# root.merge(root3)
print(root)
print(root.str_node())
"""
        Написать следующие методы:
        add(self, value: T) -> None
        search(self, value: T) -> Node[T] | None
        delete(self, value: T) -> None
        to_list(self) -> list[T]
        merge(self, other: Node[T]) -> None

        class Set (add, delete,  &,  | , is_subset,  is_empty, __init__(self, collection: Iterable[T]), __in__)
class Dict[K, V] ([K] -> V, __init__(self, collection: Iterable[tuple[K, V]]), __in__)
"""