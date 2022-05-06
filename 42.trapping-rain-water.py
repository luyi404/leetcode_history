# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc tags=array;two-pointers;stack

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
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            mn = min(height[l], height[r])
            if mn == height[l]:
                l+= 1
                while l < r and mn >= height[l]:
                    ans += mn - height[l]
                    l += 1
            else:
                r -= 1
                while l < r and mn >= height[r]:
                    ans += mn - height[r]
                    r -= 1
        return ans


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('height = [0,1,0,2,1,0,1,3,2,1,2,1]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('height = [4,2,0,3,2,5]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().trap([4,2,0,3,2,5])))
    print()
    
    pass
# @lc main=end