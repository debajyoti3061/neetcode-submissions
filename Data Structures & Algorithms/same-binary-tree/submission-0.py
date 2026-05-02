"""
REVISION NOTES - Same Binary Tree:
- Recursively compare corresponding nodes
- Check if both nodes are null (equal) or one is null (not equal)
- Compare values and recursively check left and right subtrees
- All comparisons must be true for trees to be same
- Time: O(n), Space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
        