# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#


# @lc tags=breadth-first-search

# @lc imports=start
import collections
import enum
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
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, p in flights:
            graph[s][d] = p
        pq = [(0, src, k + 1)]  # cost, source, times
        vis = [0] * n
        while pq:
            c, s, t = heappop(pq)
            if s == dst:
                return c
            if vis[s] >= t:
                continue
            vis[s] = t
            for key, v in graph[s].items():
                heappush(pq, (c + v, key, t - 1))
        return -1

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],src = 0, dst = 3, k = 1')
    print('Exception :')
    print('700')
    print('Output :')
    print(str(Solution().findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k= 1')
    print('Exception :')
    print('200')
    print('Output :')
    print(str(Solution().findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k= 0')
    print('Exception :')
    print('500')
    print('Output :')
    print(str(Solution().findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0)))
    print()
    
    pass
# @lc main=end