#!/usr/bin/env python3


class BstNode():
    def __init__(self, value=0) -> None:
        self.value = value
        self.right = None
        self.left = None

    def insert(self, val):
        if val < self.value:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BstNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BstNode(val)

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        
        print(self.value, end=" ")

        if self.right:
            self.right.traverseInOrder()

    def traversePreOrder(self):
        '#This will print in the way in which tree is traversed'
        print(self.value, end=" ")
        if self.left:
            self.left.traversePreOrder()
        
        if self.right:
            self.right.traversePreOrder()

    def traversePostOrder(self):
        '#This will print in the way in which tree is traversed'
        if self.left:
            self.left.traversePostOrder()
        
        if self.right:
            self.right.traversePostOrder()
        print(self.value, end=" ")

    def delete(self, val):
        'Delete opaeration'
        pass


root = BstNode(5)
root.insert(1)
root.insert(6)
root.insert(3)
root.insert(2)
root.insert(8)

root.traverseInOrder()
print()
root.traversePreOrder()
print()
root.traversePostOrder()


            



