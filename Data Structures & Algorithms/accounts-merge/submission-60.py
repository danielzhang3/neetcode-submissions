class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        owner = {}

        for account in accounts: 
            name = account[0]
            emails = account[1:]
            for e in emails: 
                graph[e]
                owner[e] = name
            for i in range(len(emails) - 1): 
                e1, e2 = emails[i], emails[i + 1]
                graph[e1].append(e2)
                graph[e2].append(e1)
    
        res = []
        visited = set()

        for email in graph: 
            if email in visited: 
                continue
            
            connected = []
            visited.add(email)
            q = deque()
            q.append(email)

            while q: 
                cur = q.popleft()
                connected.append(cur)
                for nei in graph[cur]: 
                    if nei in visited: 
                        continue
                    
                    visited.add(nei)
                    q.append(nei)
            
            connected.sort()
            res.append([owner[email]] + connected)
        
        return res
        