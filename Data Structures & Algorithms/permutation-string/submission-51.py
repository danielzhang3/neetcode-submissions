class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        
        target = Counter(s1)

        window = defaultdict(int)
        l = 0

        for r in range(len(s2)): 
            rc = s2[r]
            window[rc] += 1

            if (r - l + 1) > len(s1): 
                lc = s2[l]
                window[lc] -= 1
                if window[lc] == 0: 
                    del window[lc]
                l += 1
            
            if target == window: 
                return True
        
        return False
        