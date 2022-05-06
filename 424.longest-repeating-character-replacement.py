# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
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
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        left, right = 0, 0
        inside = {}
        historyMax = 0
        for right in range(n):
            inside[s[right]] = inside.get(s[right], 0) + 1
            historyMax = max(historyMax, inside[s[right]])
            if right - left + 1 > historyMax + k:
                inside[s[left]] -= 1
                left += 1
        return n - left
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ABAB", k = 2')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().characterReplacement("ABAB",2)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "AABABBA", k = 1')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().characterReplacement("AABABBA",1)))
    print()
    
    pass
# @lc main=end