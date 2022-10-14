from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any, next: 'Node') -> None:
        self.value = 5
        self.next

    def push(self,value: Any):

    def append(self, value: Any):

    def node(self, at: int):

    def insert(self, value: Any, after: Node):

class LinkedList:
    head: Node
    tail: Node

    def pop(self):

    def remove_last(self):

    def remove(self, after: Node):
