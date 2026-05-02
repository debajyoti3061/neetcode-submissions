"""
REVISION NOTES - Depth Of Binary Tree:
- Recursively calculate depth of left and right subtrees
- Return 1 + maximum of left and right depths
- Base case: return 0 for null nodes
- Can be done iteratively using level-order traversal
- Time: O(n), Space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
        