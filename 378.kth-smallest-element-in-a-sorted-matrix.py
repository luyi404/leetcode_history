# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#


# @lc tags=binary-search;heap

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
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        ans = []
        for i in range(n):
            for j in range(n):
                if len(ans) == k:
                    heappushpop(ans, -matrix[i][j])
                else:
                    heappush(ans, -matrix[i][j])
        return -heappop(ans)


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8')
    print('Exception :')
    print('13')
    print('Output :')
    print(str(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('matrix = [[-5]], k = 1')
    print('Exception :')
    print('-5')
    print('Output :')
    print(str(Solution().kthSmallest([[-5]],1)))
    print()
    
    pass
# @lc main=end