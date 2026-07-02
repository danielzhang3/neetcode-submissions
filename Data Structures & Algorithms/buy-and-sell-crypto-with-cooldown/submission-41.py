class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for i in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)): 
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        
        return max(dp[len(prices) - 1][1], dp[len(prices) - 1][2])
        