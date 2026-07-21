class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-cnt, ch) for (ch, cnt) in count.items()]
        heapq.heapify(max_heap)
        prev_cnt, prev_ch = 0, ""
        res = []

        while max_heap or prev_cnt < 0: 
            if not max_heap: 
                return ""
            
            cnt, ch = heapq.heappop(max_heap)
            res.append(ch)
            cnt += 1

            if prev_cnt < 0: 
                heapq.heappush(max_heap, (prev_cnt, prev_ch))
            
            prev_cnt, prev_ch = cnt, ch
        
        return "".join(res)
        