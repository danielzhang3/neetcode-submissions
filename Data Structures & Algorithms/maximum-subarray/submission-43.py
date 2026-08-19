class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max, res = nums[0], nums[0]

        for num in nums[1:]:
            curr_max = max(num, num + curr_max)
            res = max(res, curr_max)

        return res 
            
        