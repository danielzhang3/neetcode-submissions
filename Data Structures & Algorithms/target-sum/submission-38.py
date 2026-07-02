class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums: 
            new = defaultdict(int)
            for curr_val in dp: 
                add = curr_val + num
                subtract = curr_val - num
                new[add] += dp[curr_val]
                new[subtract] += dp[curr_val]
            dp = new
        
        return dp[target]

        