class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enq, proc, i) for i, (enq, proc) in enumerate(tasks)]
        tasks.sort(key=lambda x:x[0])

        current = []
        i = 0
        time = 0
        res = []

        while i < len(tasks) or current: 
            while i < len(tasks) and tasks[i][0] <= time: 
                enq, proc, idx = tasks[i]
                heapq.heappush(current, (proc, idx))
                i += 1
            
            if not current: 
                time = tasks[i][0]
            else: 
                proc, idx = heapq.heappop(current)
                time += proc
                res.append(idx)
        
        return res
        