# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None:
                return False
            return r1.val == r2.val and (helper(r1.left, r2.right) and helper(r1.right, r2.left))
        return helper(root, root)
        