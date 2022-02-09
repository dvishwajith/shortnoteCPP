#!/usr/bin/env python3


class TreeNode():
    def __init__(self, val=0) -> None:
        self.val = val
        self.right = None
        self.left = None


def insert(root, val):
    if root is None:
        return TreeNode(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root


root = insert(None, 5)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 8)


def inOrderTraverse(root):
    if root.left:
        inOrderTraverse(root.left)
    print(root.val)
    if root.right:
        inOrderTraverse(root.right)

def preOrderTraverse(root):
    if root.left:
        preOrderTraverse(root.left)
    print(root.val)
    if root.right:
        preOrderTraverse(root.right)
                        

def postOrderTraverse(root):
    if root.left:
        postOrderTraverse(root.left)
    print(root.val)
    if root.right:
        postOrderTraverse(root.right)


print("inOrderTraverse")
inOrderTraverse(root)
print("preOrderTraverse")
preOrderTraverse(root)
print("postOrderTraverse")
postOrderTraverse(root)



            



