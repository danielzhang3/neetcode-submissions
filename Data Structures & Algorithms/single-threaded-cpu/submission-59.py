class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enq, proc, i) for i, (enq, proc) in enumerate(tasks)]
        tasks.sort(key=lambda x:x[0])
        
        available = []
        time = 0
        i = 0
        res = []

        while i < len(tasks) or available: 
            while i < len(tasks) and tasks[i][0] <= time: 
                heapq.heappush(available, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not available: 
                time = tasks[i][0]
            else: 
                proc, idx = heapq.heappop(available)
                time += proc
                res.append(idx)
        
        return res
        