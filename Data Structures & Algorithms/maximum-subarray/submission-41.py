class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        curr_max = float("-inf")

        for num in nums: 
            curr_sum = max(num, num + curr_sum)
            curr_max = max(curr_sum, curr_max)
        
        return curr_max
        

        
        