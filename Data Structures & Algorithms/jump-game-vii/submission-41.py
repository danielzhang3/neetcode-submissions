class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[0] != "0" or s[-1] != "0": 
            return False
        
        n = len(s)
        q = deque()
        q.append(0)
        visited = [False] * n
        visited[0] = True
        far = 0

        while q: 
            i = q.popleft()
            start = max(i + minJump, far)
            end = min(i + maxJump, n - 1)
            for j in range(start, end + 1): 
                if s[j] == "0" and not visited[j]: 
                    if j == n - 1: 
                        return True
                    q.append(j)
                    visited[j] = True
            far = max(far, end + 1)
        
        return visited[n - 1]

        