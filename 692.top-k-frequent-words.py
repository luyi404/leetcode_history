# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#


# @lc tags=hash-table;heap;trie

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
class node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
    def __lt__(self, other) -> bool:
        if self.value == other.value:
            return self.key > other.key
        else:
            return self.value < other.value

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        record = {}
        for word in words:
            record[word] = record.get(word, 0) + 1
        ans = []
        for word in record:
            if len(ans) == k:
                heappushpop(ans, node(word, record[word]))
            else:
                heappush(ans, node(word, record[word]))
        res = []
        while ans:
            res.append(heappop(ans).key)
        return res[::-1]
        

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["i","love","leetcode","i","love","coding"], k = 2')
    print('Exception :')
    print('["i","love"]')
    print('Output :')
    print(str(Solution().topKFrequent(["i","love","leetcode","i","love","coding"],2)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('words =["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4')
    print('Exception :')
    print('["the","is","sunny","day"]')
    print('Output :')
    print(str(Solution().topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4)))
    print()
    
    pass
# @lc main=end