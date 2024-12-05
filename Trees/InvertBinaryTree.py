# LEETCODE 226
# Given the root of a binary tree, invert the tree, and return its root. 

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: [] 

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self._print_tree()
    
    def _print_tree(self, level=0, prefix="Root: "):
        if not self:
            return "Empty tree"
        
        result = "  " * level + prefix + str(self.val) + "\n"
        
        if self.left:
            result += self.left._print_tree(level + 1, "L--- ")
        if self.right:
            result += self.right._print_tree(level + 1, "R--- ")
        
        return result
    
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# function to construct a tree from an array
def create_tree(arr):
    if not arr:
        return None
    
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

if __name__ == "__main__":

    sol = Solution()
    # Create tree from array
    newroot = create_tree([4,2,7,1,3,6,9])
    
    # Print original tree
    print("Original Tree:")
    print(newroot)
    
    # Invert and print
    inverted_root = sol.invertTree(newroot)
    print("Inverted Tree:")
    print(inverted_root)