# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
REVISION NOTES - Level Order Traversal Of Binary Tree:
• Use BFS with queue to traverse tree level by level
• For each level, process all nodes currently in queue
• Use range(len(q)) to process exactly one level at a time
• Add children to queue for next level processing
• Collect values for each level in separate list
• Time: O(n), Space: O(w) where w is maximum width of tree
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                
                root = q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            res.append(level)
        return res
        