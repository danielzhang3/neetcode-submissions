class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: 
            return False
        
        target = total // k
        nums.sort(reverse = True)
        if nums[0] > target: 
            return False
        
        subsets = [0] * k

        def dfs(i): 
            if i == len(nums): 
                return all(s == target for s in subsets)
            
            for j in range(k): 
                if j > 0 and subsets[j] == subsets[j - 1]: 
                    continue
                
                if subsets[j] + nums[i] <= target: 
                    subsets[j] += nums[i]
                    if dfs(i + 1): 
                        return True
                    subsets[j] -= nums[i]
                
                if subsets[j] == 0: 
                    break
            return False
        
        return dfs(0)
        

        