# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#


# @lc tags=hash-table;binary-search

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
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        record = dict()
        for i in nums1:
            for j in nums2:
                record[i + j] = record.get(i + j, 0) + 1
        for i in nums3:
            for j in nums4:
                ans += record.get(-i - j, 0)
        return ans
        
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().fourSumCount([1,2],[-2,-1],[-1,2],[0,2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().fourSumCount([0],[0],[0],[0])))
    print()
    
    pass
# @lc main=end