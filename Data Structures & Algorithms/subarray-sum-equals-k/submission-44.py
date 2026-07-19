class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        res = 0
        curr_sum = 0

        for num in nums: 
            curr_sum += num
            diff = curr_sum - k
            res += prefix.get(diff, 0)
            prefix[curr_sum] = 1 + prefix.get(curr_sum, 0)
        
        return res
        