# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#


# @lc tags=tree

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
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        m = [[float('inf')] * n for _ in range(n)]
        for s, d, t in times:
            m[s-1][d-1] = t
        dist = [float('inf')] * n
        dist[k - 1] = 0
        used = set()
        for _ in range(n):
            x = -1
            for i in range(n):
                if i not in used and (x == -1 or dist[x] > dist[i]):
                    x = i
            used.add(x)
            for i, time in enumerate(m[x]):
                dist[i] = min(dist[i], time + dist[x])
        return max(dist) if max(dist) != float('inf') else -1



# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('times = [[1,2,1]], n = 2, k = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().networkDelayTime([[1,2,1]],2,1)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('times = [[1,2,1]], n = 2, k = 2')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().networkDelayTime([[1,2,1]],2,2)))
    print()
    
    pass
# @lc main=end