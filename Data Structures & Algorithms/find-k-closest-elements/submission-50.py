class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        low, high = 0, n - k

        while low < high: 
            m = (low + high) // 2
            left_gap = x - arr[m]
            right_gap = arr[m + k] - x

            if left_gap > right_gap: 
                low = m + 1
            else: 
                high = m
        
        return arr[low: low + k]

        