# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        maxLevel = 0

        def rightView(root,level):
            nonlocal res
            nonlocal maxLevel
            if not root:
                return
            if maxLevel < level:
                res.append(root.val)
                maxLevel = level
            rightView(root.right,level+1)
            rightView(root.left,level+1)
        rightView(root,1)
        return res


        