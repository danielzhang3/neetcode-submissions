class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        res = float("-inf")

        for num in nums: 
            curr_max = max(num, num + curr_max)
            res = max(res, curr_max)
        
        return res

        