"""
REVISION NOTES - Binary Tree Inorder Traversal:
- Recursive: left subtree -> root -> right subtree
- Iterative: use stack to simulate recursion
- For BST, inorder gives sorted sequence
- Time: O(n), Space: O(h) for recursion stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res
        