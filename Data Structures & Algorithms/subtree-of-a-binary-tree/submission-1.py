# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
REVISION NOTES - Subtree of a Binary Tree:
• Two-step approach: check if trees are same + recursively check subtrees
• Helper function sameTree() checks if two trees are identical
• Main function checks if subRoot matches current node or exists in left/right subtrees
• Base cases: null subRoot is always subtree, null root with non-null subRoot is false
• Recursive calls on left and right children to find matching subtree
• Time: O(m*n) where m,n are sizes of trees, Space: O(h) for recursion depth
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def sameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return sameTree(s.left, t.left) and sameTree(s.right, t.right)
        
        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)