# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node: return 0, 0
            lval, lcount = dfs(node.left)
            rval, rcount = dfs(node.right)
            nval, ncount = lval + rval + node.val, lcount + rcount + 1
            if nval // ncount == node.val: self.res += 1
            return nval, ncount
        dfs(root)
        return self.res
        