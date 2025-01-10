from __future__ import annotations
from abc import ABCMeta, abstractmethod
from enum import Enum, auto
from typing import Any, Callable, Iterable, TypeVar
from tree import Node
import copy

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

T = TypeVar('T', bound='Comparable')

class AVLNode(Node):
    height: int

    def __init__(
        self,
        value: T,
        predicate: Callable = lambda first, second: (
            Compare.Less
            if first < second
            else (Compare.Greater if first > second else Compare.Equal)
        ),
    ) -> None:
        
        super().__init__(value, predicate)
        #self.value = value
        self.height = 1 # У корня будеть высота

    def __str__(self, level=0):
        result = " " * (level * 4) + '|' + str(self.value) + "\n"
        if self.left:
            result += 'l' + self.left.__str__(level + 1)
        if self.right:
            result += 'r' + self.right.__str__(level + 1)
        return result
    
    def update_height(self):
        """Меняет высоту, если это необходимо"""
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = 1 + max(left_height, right_height)

    def update_height_del(self):
        """Уменьшает высоту после удаления вершины"""

    def _replace_self(self, new_node: AVLNode[T]) -> None:
        self.value = new_node.value
        self.left = new_node.left
        self.right = new_node.right
        self.height = new_node.height
        self.predicate = new_node.predicate
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
    def get_height(self):
        if self: # То есть оно не None
            return self.height
        return 0
    
    def get_child_height(self, lr=""): # некрасиво, но лучше чем каждый раз проверять на существование
        if lr == "r":
            if self.right is None:
                return 0
            return self.right.height
        if self.left is None:
            return 0
        return self.left.height 

    def correct(self) -> bool:
        """проход по дереву по сути"""
        # print("Высота правого", self.right.height)
        # print("Высота левого", self.left.height)

        if (self.left is None and self.get_child_height("r") >= 1) or (self.right is None and self.get_child_height("l") >= 1):
            #print('matched!')
            return False 
        elif abs(self.get_child_height("r") - self.get_child_height("l")) > 1:
            return False
        left_correct = self.left.correct() if self.left else True
        right_correct = self.right.correct() if self.right else True

        return left_correct and right_correct

    def rotate_left(self):
        if self.right is None:
            return self  
        new = self.right
        self.right = new.left
        new.left = self
        return new
    
    def rotate_right(self):
        if self.left is None:
            return self  
        new = self.left
        self.left = new.right
        new.right = self
        return new
        
    def balance(self) -> None:
        self.height += 1
        diff =  self.get_child_height("l") - self.get_child_height("r")
        if diff > 1:
                l =  self.left.get_child_height("l")- self.left.get_child_height("r")
                if l >= 0:
                    # Малое правое вращение 
                    return self.rotate_right()
                else:
                    # Большое правое вращение 
                    self.left = self.left.rotate_left()
                    return self.rotate_right()
        elif diff < -1:
            r =  self.right.get_child_height("l")- self.right.get_child_height("r")
            if r <= 0:
                    # Малое левое вращение 
                return self.rotate_left()
            else:
                    # Большое левое вращение 
                self.right = self.right.rotate_right()
                return self.rotate_left()
        self.update_height()
        return self

    def add(self, value: T) -> None:
        """ Добавление элемента, потом балансируется родительский узел"""
        # print("значени", value, "дерево" ,self)
        if self.predicate(value, self.value) == Compare.Less:
            if self.left is None:
                self.left = AVLNode(value, self.predicate)
                self.left.parent = self # Установка родителя  # я смотрю на узел в который добавляли, а не то, что добавили!
            else:
                self.left.add(value)
        elif self.predicate(value, self.value) == Compare.Greater:
            if self.right is None:
                self.right = AVLNode(value, self.predicate)
                self.right.parent = self

            else:
                self.right.add(value)
        self.update_height()
        return self.balance()

    def search(self, value: T) -> AVLNode[T] | None:

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
        """Your code here"""
        # del_node = self.search(value)
        # if self.right is None and self.left is None:
        #     if del_node.find_parent_pos() == "left":
        #         del_node.parent.left = None
        #         del_node.parent.height = del_node.parent.right.get_height()
        #     else:
        #         del_node.parent.right = None
        #         del_node.parent.height = del_node.parent.left.get_height()
            
        super().delete(value)
        self.balance()

    def merge(self, other: AVLNode[T]) -> None:
        """YOur code here"""
        #super().merge(other)
        other_elems = other.to_list()
        for elem in other_elems:
            self.add(elem)
            


class AVLSet:
    node: AVLNode[T] | None

    def __init__(self, collection: Iterable[T]):
        self.node: AVLNode[T: Comparable] | None = None
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

    def __or__(self, other: AVLSet) -> AVLSet: # Пересечение n * log(m)
        """
        Персечение множеств
        """
        inter = AVLSet([])
        for i in self.node.to_list():
            if other.node.search(i):
                inter.add(i)
        return inter

    def __and__(self, other: AVLSet) -> AVLSet: # Объединения n * m + (n+m)
        """
        Объединение множеств
        """
        self.node.merge(other.node)
        return AVLSet(self.node.to_list())
    

    def is_subset(self, other: AVLSet) -> bool: # log(n)*m
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


class AVLDict:
    node: AVLNode[T: Comparable]

    def __init__(self, collection: Iterable[tuple[K, V]]):
        """
        Иницализация
        """
        self.collection = collection
        self.node: AVLNode[T: Comparable] | None = None
        for value in collection:
            if self.node is None:
                self.node = AVLNode(value)
            else:
                self.node.add(value)

    def str_node(self):
        return self.node.__str__()

    def __repr__(self) -> str:
        return "<dict  representation>"
    

    def search_tuple(self, node: AVLNode[T], value: Comparable) -> AVLNode[tuple] | None:
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
    
    def del_by_indx(self, indx: int) -> None:
        del_elem = self.node.to_list()[indx]
        self.node.delete(del_elem) 