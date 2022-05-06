# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#


# @lc tags=dynamic-programming

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
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0, 0, 0] for _ in range(n)]
        # 不持有也没卖
        # 持有
        # 不持有 因为卖了
        dp[0] = [0, -prices[0], 0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
        return max(dp[n - 1][0], dp[n - 1][2])

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [1,2,3,0,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maxProfit([1,2,3,0,2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('prices = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxProfit([1])))
    print()
    
    pass
# @lc main=end