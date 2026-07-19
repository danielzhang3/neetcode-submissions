class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t0, t1, t2 = target
        found = [False] * 3

        for a, b, c in triplets: 
            if a <= t0 and b <= t1 and c <= t2: 
                if a == t0: 
                    found[0] = True
                if b == t1: 
                    found[1] = True
                if c == t2: 
                    found[2] = True
        
        return all(found)
        