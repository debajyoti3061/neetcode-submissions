"""
REVISION NOTES - Binary Tree Postorder Traversal:
- Recursive: left subtree -> right subtree -> root
- Iterative: use stack with visited tracking
- Useful for deleting trees (children before parent)
- Time: O(n), Space: O(h) for recursion stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def post(node):
            if not node:
                return
            post(node.left)
            post(node.right)
            res.append(node.val)
        post(root)
        return res
        