# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc tags=array;two-pointers

# @lc imports=start
from operator import le
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
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        ans = 0
        while left < right:
            ans = max((right - left) * min(height[left], height[right]), ans)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans
    
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('height = [1,8,6,2,5,4,8,3,7]')
    print('Exception :')
    print('49')
    print('Output :')
    print(str(Solution().maxArea([1,8,6,2,5,4,8,3,7])))
    print()
    
    # print('Example 2:')
    # print('Input : ')
    # print('height = [1,1]')
    # print('Exception :')
    # print('1')
    # print('Output :')
    # print(str(Solution().maxArea([1,1])))
    # print()
    
    pass
# @lc main=end