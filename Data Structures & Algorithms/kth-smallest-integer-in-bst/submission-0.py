# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
REVISION NOTES - Kth Smallest Integer In BST:
• Use iterative inorder traversal with stack
• Inorder traversal of BST visits nodes in ascending order
• Go left as far as possible, then process current node
• Count nodes processed until reaching kth node
• Return value of kth node when counter reaches k
• Time: O(H + k), Space: O(H) where H is tree height
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

        