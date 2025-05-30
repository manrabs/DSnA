# Binary Tree implementation
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return(self.val)
    
# recursive pre order traversal (dfs) time: O(n), space: O(n) -> process node, left, right
def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

# recursive in order traversal -> left, process node, right
def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)

# recursive post order traversal -> left, right, process node
def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)

# Iterative traversal dfs (always pre order i think)
def iterative(node):
    stack = [node]
    while stack:
        node = stack.pop()
        print(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# level order traversal (BFS) time: O(n), space: O(n)
from collections import deque
def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: 
            q.append(node.left)
        if node.right:
            q.append(node.right)

# check if a value exists (dfs) time: O(n), space O(n)
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

# same function as above but for a binary search tree

def search_bst(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    
    # REMEMBER:
    # all values on left side of bst are less than the root/current node value
    # all values on right side of bst are greater than root/current node value
    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)