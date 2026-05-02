"""
REVISION NOTES - Invert A Binary Tree:
- Recursively swap left and right children of each node
- Base case: return null for null nodes
- Swap children, then recursively invert subtrees
- Can be done iteratively using queue/stack
- Time: O(n), Space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        