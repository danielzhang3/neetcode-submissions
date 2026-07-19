class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        required = len(target)
        
        window = defaultdict(int)
        formed = 0

        res_len, res_l, res_r = float("inf"), 0, 0
        l = 0

        for r in range(len(s)): 
            rc = s[r]
            window[rc] += 1

            if (rc in target and window[rc] == target[rc]): 
                formed += 1
            
            while formed == required: 
                if r - l + 1 < res_len: 
                    res_len = r - l + 1
                    res_l = l
                    res_r = r
                
                lc = s[l]
                window[lc] -= 1
                if (lc in target and window[lc] < target[lc]): 
                    formed -= 1
                l += 1

        
        return s[res_l: res_r + 1] if res_len != float("inf") else ""
        