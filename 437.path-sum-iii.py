# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().pathSum(listToTreeNode([10,5,-3,3,2,None,11,3,-2,None,1]),8)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().pathSum(listToTreeNode([5,4,8,11,None,13,4,7,2,None,None,5,1]),22)))
    print()
    
    pass
# @lc main=end