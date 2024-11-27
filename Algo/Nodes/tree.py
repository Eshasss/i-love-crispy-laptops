from __future__ import annotations
from abc import ABCMeta, abstractmethod
from enum import Enum, auto
from typing import Any, Callable, Iterable, TypeVar

T = TypeVar('T', bound='Comparable')

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
        """
        Иницализация
        """
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
        """
        Проверяет валидность дерева
        """
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
        """
        Добавляет новый элемент.
        """
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
        """
        Поиск элемента  в дереве и возращает поддерево искомой вершины.
        """
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

    def find_min(self) -> Node[T]:
        """
        Минимальную дочь дерева.
        """
        while self.left:
            self = self.left # так делать нехорошо но оно работает??
        return self

    def find_parent_pos(self) -> str:
        """
        Узнает позицию стороны родителя
        """
        if self.parent.right == self:
            return "right"
        else:
            return "left"

    def delete(self, value: T) -> None:
        """
        Удаляет элемент из дерева.
        """
        del_node = self.search(value)
        
        if del_node is None:
            raise ValueError(f"Value {del_node.value} is not in the tree.")
        if value == self.value: # Главный корень
            r_r = del_node.right.right
            r_l = del_node.right.left
            addon = self.left
            self.value = del_node.right.value
            self.right = r_r
            self.left = r_l
            self.left.find_min().left = addon
        elif del_node.left is None and del_node.right is None: # Лист
            if del_node.find_parent_pos() == "left":
                del_node.parent.left = None
            else:
                del_node.parent.right = None
        elif del_node.left is not None and del_node.right is not None: # 2 поддерева
            if del_node.find_parent_pos() == "right":
                del_node.parent.right = del_node.right
                del_node.parent.right.find_min().left = del_node.left 
            else:
                del_node.parent.left = del_node.left
                del_node.parent.left.find_min().right = del_node.right 
        elif del_node.left is not None or del_node.right is not None: # 1 поддерево
            addon = del_node.left or del_node.right  # значение единственного поддерева
            if del_node.find_parent_pos() == 'left':
                del_node.parent.left = addon
            else:
                del_node.parent.right = addon
            addon.parent = del_node.parent

    def to_list(self) -> list[T]:
        """
        Создает отсортированный список всех элементов ноды.
        """
        values = []
        if self.left is not None:
            values.extend(self.left.to_list())
        values.append(self.value)
        if self.right is not None:
            values.extend(self.right.to_list())
        return values

    def merge(self, other: Node[T]) -> None:
        """
        Слияние двух нод.
        """
        other_elems = other.to_list()
        for elem in other_elems:
            self.add(elem)


class Set:

    node: Node[T] | None

    def __init__(self, collection: Iterable[T]):
        self.node: Node[T: Comparable] | None = None
        for val in collection:
            self.add(val)

    def add(self, value: T) -> None:
        """
        Добавляет элемент во множество
        """
        if self.node is None:
            self.node = Node(value)
        else:
            self.node.add(value)

    def __str__(self) -> str:
        vals = self.node.to_list()
        return f"{{{", ".join(map(str, vals))}}}"
    
    def __repr__(self) -> str:
        return "<set>"
    
    def str_node(self):
        """
        Множество в виде дерева
        """
        return self.node.__str__()

    def delete(self, value: Any) -> None:
        """
        Удаляет элемент во множестве
        """
        self.node.delete(value)

    def __or__(self, other: Set) -> Set: # Пересечение n * log(m)
        """
        Персечение множеств
        """
        inter = Set([])
        for i in self.node.to_list():
            if other.node.search(i):
                inter.add(i)
        return inter

    def __and__(self, other: Set) -> Set: # Объединения n * m + (n+m)
        """
        Объединение множеств
        """
        self.node.merge(other.node)
        return Set(self.node.to_list())
    

    def is_subset(self, other: Set) -> bool: # log(n)*m
        """
        Проверка на подмножество
        """

        if self.node.search(other.node.value) is None:
            return False
        if other.node.left is not None:
            self.node.search(other.node.left.value) 
        if other.node.right is not None:
            self.node.search(other.node.right.value)
        return True
    

    def is_empty(self) -> bool:
        """
        Проверка на пустоту
        """
        if self.node is None:
            return True
        return False

    def __contains__(self, val: Any) -> bool: #log(n)
       
       search_res = self.node.search(val)
       if search_res:
           return True
       return False


class Dict:

    node: Node[T: Comparable]

    def __init__(self, collection: Iterable[tuple[K, V]]):
        """
        Иницализация
        """
        self.collection = collection
        self.node: Node[T: Comparable] | None = None
        for value in collection:
            if self.node is None:
                self.node = Node(value)
            else:
                self.node.add(value)
    # def __str__(self) -> str:
    #     strver = "{"
    #     for val in self.collection:
    #         strver += f'{val[0]}: {val[1]}'
    #     print(type(strver))
    #     return  strver + '}'

    def str_node(self):
        return self.node.__str__()

    def __repr__(self) -> str:
        return "<dict  representation>"
    

    def search_tuple(self, node: Node[T], value: Comparable) -> Node[tuple] | None:
        """
        Поиск элемента для вершин кортежей. 
        """
        if self.node.predicate(value, node.value[0]) == Compare.Equal:
            return True
        if self.node.predicate(value, node.value[0]) == Compare.Less:
            if node.left is None:
                return False
            return self.search_tuple(node.left, value)
        if self.node.predicate(value, node.value[0]) == Compare.Greater:
            if node.right is None:
                return False
            return self.search_tuple(node.right, value)
    
    def __contains__(self, value) -> bool:
        if self.search_tuple(self.node, value):
            return True
        return False


# node = Node(8)
# node.add(4)
# node.add(7)
# node.add(8)
# node.add(23)
# node.add(12)
# print(node)
# node2 = Node(12)
# node2.add(6)
# node2.add(10)
# node2.add(38)
# node2.add(3)
# node2.add(2)

# node.merge(node2)
# print(node)

# print(node.correct())
# node.search(10)

# set1 = Set([('hello', 1), ('world', [1,2,3]), ('how', 123.5), ('are', 'you')])
# set2 = Set([('hello', 1), ('world', [1,2,3]), ('abracadabra', 71)])
# print(set1&set2)
# print(set1|set2)
# print(set2.is_subset(set1))

# dict1 = Dict([('hello', 1), ('world', [1,2,3]), ('how', 123.5), ('are', 'you')])
# print(dict1)


# set1 = Set([1, 2, 3])
# set2 = Set([3, 4, 5])
# print(set1.is_subset(set2))
# print(set2.is_subset(set1))
