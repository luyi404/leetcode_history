# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc tags=hash-table;two-pointers;string;sliding-window

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
    def helper(self, trecord, srecord, tleft, left, c) -> bool:
        if tleft == left:
            flag = True
            for key in trecord.keys():
                if key in srecord and srecord[key] >= trecord[key]:
                    continue
                else:
                    flag = False
                    break
            return flag
        else:
            return c not in trecord or srecord[c] >= trecord[c]

    def minWindow(self, s: str, t: str) -> str:
        trecord = {}
        for c in t:
            trecord[c] = trecord.get(c, 0) + 1
        left = 0
        srecord = {}
        historyMinLength, ans = 100001, ''
        for right in range(len(s)):
            srecord[s[right]] = srecord.get(s[right], 0) + 1
            tleft = left
            while self.helper(trecord, srecord, tleft, left, s[left - 1]):
                if right - left + 1 < historyMinLength:
                    historyMinLength = right - left + 1
                    ans = s[left: right + 1]
                srecord[s[left]] -= 1
                left += 1
        return ans
                

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ADOBECODEBANC", t = "ABC"')
    print('Exception :')
    print('"BANC"')
    print('Output :')
    print(str(Solution().minWindow("ADOBECODEBANC","ABC")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "a", t = "a"')
    print('Exception :')
    print('"a"')
    print('Output :')
    print(str(Solution().minWindow("a","a")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "a", t = "aa"')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().minWindow("a","aa")))
    print()
    
    pass
# @lc main=end