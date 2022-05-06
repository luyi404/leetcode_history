# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


# @lc tags=array;two-pointers

# @lc imports=start
from operator import le
import tarfile
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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            left, right = i + 1, n - 1
            sub_target = target - nums[i]
            while left < right:
                twosum = nums[left] + nums[right]
                if abs(sub_target - twosum) < diff:
                    ans = twosum + nums[i]
                    diff = abs(sub_target - twosum)
                if twosum > sub_target:
                    right -= 1
                else:
                    left += 1
        return ans
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-1,2,1,-4], target = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().threeSumClosest([-1,2,1,-4],1)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [0,0,0], target = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().threeSumClosest([0,0,0],1)))
    print()
    
    pass
# @lc main=end