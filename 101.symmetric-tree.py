# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#


# @lc tags=tree;depth-first-search;breadth-first-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
# 
# 
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if (not left and right) or (left and not right) or (left.val != right.val):
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,2,3,4,4,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isSymmetric(listToTreeNode([1,2,2,2,None,2]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1,2,2,null,3,null,3]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isSymmetric(listToTreeNode([1,2,2,None,3,None,3]))))
    print()
    
    pass
# @lc main=end