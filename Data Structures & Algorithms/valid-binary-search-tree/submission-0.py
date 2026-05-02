"""
REVISION NOTES - Valid Binary Search Tree:
- Use inorder traversal to check if values are in ascending order
- Or recursively check with min/max bounds for each subtree
- Left subtree values must be less than root
- Right subtree values must be greater than root
- Time: O(n), Space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isBST(root,min,max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False
            return isBST(root.left,min,root.val) and isBST(root.right,root.val,max)
        
        return isBST(root,float("-inf"),float("inf"))
        