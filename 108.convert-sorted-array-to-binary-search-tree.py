# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#


# @lc tags=tree;depth-first-search

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
    def helper(self, nums, left, right):
        if left > right:
            return None
        mid = (right + left) // 2
        node = TreeNode(val=nums[mid])
        node.left = self.helper(nums, left, mid - 1)
        node.right = self.helper(nums, mid + 1, right)
        return node
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)
        

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-10,-3,0,5,9]')
    print('Exception :')
    print('[0,-3,9,-10,null,5]')
    print('Output :')
    print(str(Solution().sortedArrayToBST([-10,-3,0,5,9])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,3]')
    print('Exception :')
    print('[3,1]')
    print('Output :')
    print(str(Solution().sortedArrayToBST([1,3])))
    print()
    
    pass
# @lc main=end