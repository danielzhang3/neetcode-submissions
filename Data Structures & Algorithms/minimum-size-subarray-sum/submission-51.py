class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        l = 0
        res = float("inf")

        for r in range(len(nums)): 
            curr_sum += nums[r]

            while curr_sum >= target: 
                if r - l + 1 < res: 
                    res = r - l + 1
                
                curr_sum -= nums[l]
                l += 1
        
        return res if res != float("inf") else 0
        