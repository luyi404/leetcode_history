# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc tags=array;two-pointers

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
class Solution:
    def swap(self, nums, i, j) -> None:
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while i < len(nums):
            if nums[i] != 0:
                self.swap(nums, i, j)
                j += 1
            i += 1

        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [0,1,0,3,12]')
    print('Exception :')
    print('[1,3,12,0,0]')
    print('Output :')
    print(str(Solution().moveZeroes([0,1,0,3,12])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().moveZeroes([0])))
    print()
    
    pass
# @lc main=end