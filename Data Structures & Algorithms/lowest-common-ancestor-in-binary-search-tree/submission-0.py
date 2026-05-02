# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
REVISION NOTES - Lowest Common Ancestor In Binary Search Tree:
• Leverage BST property: left < root < right
• If both p and q are smaller than current node, go left
• If both p and q are larger than current node, go right
• Otherwise, current node is the LCA (split point)
• No need for recursion, can use iterative approach
• Time: O(h), Space: O(1) where h is tree height
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur
        