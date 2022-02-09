#!/usr/bin/env python3


from collections import deque


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
    print(root.val, end=" ")
    if root.right:
        inOrderTraverse(root.right)

def preOrderTraverse(root):
    print(root.val, end=" ")
    if root.left:
        preOrderTraverse(root.left)
    if root.right:
        preOrderTraverse(root.right)
                        

def postOrderTraverse(root):
    if root.left:
        postOrderTraverse(root.left)
    if root.right:
        postOrderTraverse(root.right)
    print(root.val, end=" ")


def levelOrderTraversal(root):
    queue = deque()
    queue.append(root)

    while queue:
        #pop a node from the fron
        node = queue.popleft() 
        print(node.val, end=" ")
        # Adding children to the end of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("\ninOrderTraverse ")
inOrderTraverse(root)
print("\npreOrderTraverse ")
preOrderTraverse(root)
print("\npostOrderTraverse ")
postOrderTraverse(root)

print("\nlevelOrderTraversal ")
levelOrderTraversal(root)



            



