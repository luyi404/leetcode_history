# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#


# @lc tags=array;hash-table;binary-search;dynamic-programming

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
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def getLengh(offsetA: int, offsetB: int, length: int) -> int:
            res = k = 0
            for i in range(length):
                if nums1[offsetA + i] == nums2[offsetB + i]:
                    k += 1
                    res = max(res, k)
                else:
                    k = 0
            return res
        m, n = len(nums1), len(nums2)
        ans = 0
        for i in range(m):
            length = min(n, m - i)
            ans = max(getLengh(i, 0, length), ans)
        for j in range(n):
            length = min(m, n - j)
            ans = max(getLengh(0, j, length), ans)
        return ans
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findLength([1,2,3,2,1],[3,2,1,4,7])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findLength([0,0,0,0,0],[0,0,0,0,0])))
    print()
    
    pass
# @lc main=end