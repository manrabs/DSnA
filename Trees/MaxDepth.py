# LEETCODE 104
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# function to construct a tree from an array
def create_tree(arr):
    if not arr: return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]

    for i in range(len(nodes)):
        if nodes[i]:
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]
    return nodes[0]

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return 1 + max(left, right)
    
if __name__ == '__main__':
    tree = [3,9,20,None,None,15,7]
    newroot = create_tree(tree)
    sol = Solution()
    # print(f"total amount of nodes in tree is {len(tree)}")
    print(f"maximum depth of tree is {sol.maxDepth(newroot)}")
