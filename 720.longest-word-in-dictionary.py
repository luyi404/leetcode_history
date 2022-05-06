# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#


# @lc tags=hash-table;trie

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
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        record = set()
        ans = ""
        record.add(ans)
        for word in words:
            if word[:-1] in record:
                if len(word) > len(ans):
                    ans = word
                record.add(word)
        return ans
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["w","wo","wor","worl","world"]')
    print('Exception :')
    print('"world"')
    print('Output :')
    print(str(Solution().longestWord(["w","wo","wor","worl","world"])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('words = ["a","banana","app","appl","ap","apply","apple"]')
    print('Exception :')
    print('"apple"')
    print('Output :')
    print(str(Solution().longestWord(["a","banana","app","appl","ap","apply","apple"])))
    print()
    
    pass
# @lc main=end