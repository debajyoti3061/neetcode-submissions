"""
REVISION NOTES - Binary Tree Diameter:
- For each node, calculate longest path through that node
- Path through node = left height + right height
- Recursively calculate heights and update global maximum
- Use global variable to track maximum diameter seen
- Time: O(n), Space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res,left+right)

            return 1+ max(left,right)

        dfs(root)
        return res
        