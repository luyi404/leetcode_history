# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_length = -float('inf')
        self.m = dict()
        self.helper(root)
        return self.max_length
    def helper(self, root: TreeNode):
        if not root:
            return 0
        else:
            if root in self.m:
                return self.m[root]
            lmax = self.helper(root.left)
            rmax = self.helper(root.right)
            self.max_length = max(self.max_length, lmax + rmax)
            self.m[root] = max(lmax, rmax) + 1
            return self.m[root]
            

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,5]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().diameterOfBinaryTree(listToTreeNode([1,2,3,4,5]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().diameterOfBinaryTree(listToTreeNode([1,2]))))
    print()
    
    pass
# @lc main=end