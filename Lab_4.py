from typing import Any, List, Callable, Union
from graphviz import *


class TreeNode:
    value: Any
    children: List['TreeNode']


    def __init__(self, value: Any) -> None:
        self.value = value
        self.children = []


    def is_leaf(self) -> bool:
        if self.children == []:
            return True
        else:
            return False


    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)


    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for a in self.children:
            a.for_each_deep_first(visit)


    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        a=[]
        a.append(self)
        while a:
            visit(a[0])
            for i in a[0].children:
                a.append(i)
            a.pop(0)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for a in self.children:
            if a.search(value):
                return a.search(value)
        return None

    def show(self, pic=Digraph('Tree')):
        pic.node(str(self), str(self.value))
        for a in self.children:
            pic.edge(str(self), str(a))
            a.show(pic)
        return pic

class Tree:
    root: 'TreeNode'

    def __init__(self, root: "TreeNode") -> None:
        self.root = root


    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(TreeNode(value))


    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)


    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)


    def show(self) -> None:
        self.root.show().render(filename='tree', format='jpg', view=True)


def show_node(wsk: 'TreeNode') -> None:
    if isinstance(wsk, TreeNode):
        print(wsk.value)
    else:
        print(wsk)


# node = TreeNode('A')
# node.add(TreeNode('B'))
# node.add(TreeNode('D'))
# node.children[0].add(TreeNode('C'))
#
# tree = Tree(node)
# tree.add('E', tree.root.children[1])
# tree.add('F', tree.root.search('E'))
# tree.add('G', tree.root.search('F'))

node = TreeNode(1)
node.add(TreeNode(2))
node.add(TreeNode(4))
node.children[0].add(TreeNode(3))

tree = Tree(node)
tree.add(5, tree.root.children[1])
tree.add(6, tree.root.search(5))
tree.add(7, tree.root.search(6))

print(tree.root.is_leaf())
# print(tree.root.search(G).is_leaf())
# print(tree.root.search(F))
print(tree.root.search(6).is_leaf())
print(tree.root.search(7))

tree.for_each_deep_first(show_node)
print('----------------------------')
tree.for_each_level_order(show_node)
tree.show()