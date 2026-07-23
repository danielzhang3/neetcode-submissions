class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for ch, cnt in (("a", a), ("b", b), ("c", c)): 
            if cnt > 0: 
                heapq.heappush(max_heap, (-cnt, ch))
        res = []

        while max_heap: 
            cnt, ch = heapq.heappop(max_heap)

            if len(res) >= 2 and res[-1] == ch and res[-2] == ch: 
                if not max_heap: 
                    break
                
                cnt2, ch2 = heapq.heappop(max_heap)
                res.append(ch2)
                cnt2 += 1

                if cnt2 < 0: 
                    heapq.heappush(max_heap, (cnt2, ch2))
                heapq.heappush(max_heap, (cnt, ch))
            else: 
                res.append(ch)
                cnt += 1
                if cnt < 0: 
                    heapq.heappush(max_heap, (cnt, ch))
        
        return "".join(res)
        