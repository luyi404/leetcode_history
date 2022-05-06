# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#


# @lc tags=two-pointers;sliding-window

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
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while stones:
            s1 = -heappop(stones)
            if not stones:
                return s1
            s2 = -heappop(stones)
            if s1 > s2:
                heappush(stones, s2 - s1)
        return 0

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('stones = [2,7,4,1,8,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lastStoneWeight([2,7,4,1,8,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('stones = [1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lastStoneWeight([1])))
    print()
    
    pass
# @lc main=end