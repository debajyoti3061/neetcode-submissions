"""
REVISION NOTES - Balanced Binary Tree:
- For each node, check if height difference between subtrees <= 1
- Recursively check if left and right subtrees are balanced
- Use helper function to calculate height of subtree
- Can optimize to O(n) by calculating height and balance in single pass
- Time: O(n²) naive, O(n) optimized, Space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left-right)>1 : return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self,root):
        if not root:
            return 0
        return 1 + max(self.height(root.left),self.height(root.right))
        