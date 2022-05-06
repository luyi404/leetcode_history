# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        result = list()
        nums.sort()
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return result
                    
            
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-1,0,1,2,-1,-4]')
    print('Exception :')
    print('[[-1,-1,2],[-1,0,1]]')
    print('Output :')
    print(str(Solution().threeSum([-1,0,1,2,-1,-4])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().threeSum([])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().threeSum([0])))
    print()
    
    pass
# @lc main=end