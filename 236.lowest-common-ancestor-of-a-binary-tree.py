# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#


# @lc tags=tree

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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        self.mem = None
        self.h2(root, p, q)
        return self.mem

    def helper(self, root: 'TreeNode', p: 'TreeNode'):
        if not root:
            return False
        if root == p:
            return True
        if self.helper(root.left, p) or self.helper(root.right, p):
            return True
    
    def h2(self, root, p, q):
        if not root:
            return False
        if (self.helper(root.left, p) and self.helper(root.right, q)) or (self.helper(root.left, q) and self.helper(root.right, p)):
            self.mem = root
            return True
        if root.left:
            self.h2(root.left, p, q)
        if root.right:
            self.h2(root.right, p, q)

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().lowestCommonAncestor([3,5,1,6,2,0,8,None,None,7,4],5,1)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().lowestCommonAncestor([3,5,1,6,2,0,8,None,None,7,4],5,4)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [1,2], p = 1, q = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lowestCommonAncestor([1,2],1,2)))
    print()
    
    pass
# @lc main=end