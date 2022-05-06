# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#


# @lc tags=hash-table;heap

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
    def frequencySort(self, s: str) -> str:
        record = {}
        for c in s:
            record[c] = record.get(c, 0) + 1
        ans = []
        for c in record:
            heappush(ans, (-record[c], c))
        res = ''
        while ans:
            times, c = heappop(ans)
            for _ in range(-times):
                res += c
        return res
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "tree"')
    print('Exception :')
    print('"eert"')
    print('Output :')
    print(str(Solution().frequencySort("tree")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "cccaaa"')
    print('Exception :')
    print('"aaaccc"')
    print('Output :')
    print(str(Solution().frequencySort("cccaaa")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "Aabb"')
    print('Exception :')
    print('"bbAa"')
    print('Output :')
    print(str(Solution().frequencySort("Aabb")))
    print()
    
    pass
# @lc main=end