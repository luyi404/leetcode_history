# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#


# @lc tags=stack

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
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = {}
        stk = []
        n = len(nums2)
        for i in range(n):
            while stk and nums2[i] > nums2[stk[-1]]:
                record[nums2[stk.pop()]] = nums2[i]
            stk.append(i)
        ans = []
        for i in nums1:
            ans.append(record.get(i, -1))
        return ans


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [4,1,2], nums2 = [1,3,4,2]')
    print('Exception :')
    print('[-1,3,-1]')
    print('Output :')
    print(str(Solution().nextGreaterElement([4,1,2],[1,3,4,2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums1 = [2,4], nums2 = [1,2,3,4]')
    print('Exception :')
    print('[3,-1]')
    print('Output :')
    print(str(Solution().nextGreaterElement([2,4],[1,2,3,4])))
    print()
    
    pass
# @lc main=end