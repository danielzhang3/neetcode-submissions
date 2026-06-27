class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set()
        for combo in deadends: 
            dead.add(combo)

        if "0000" in dead: 
            return -1

        q = deque()
        q.append("0000")
        visited = set()
        visited.add("0000")

        def neighbors(code): 
            res = []
            for i in range(4): 
                digit = int(code[i])
                for move in (+1, -1): 
                    next_digit = (digit + move) % 10 
                    nxt = code[:i] + str(next_digit) + code[i + 1:]
                    res.append(nxt)
            return res

        moves = 0
        while q: 
            for i in range(len(q)): 
                combo = q.popleft()
                if combo == target: 
                    return moves
                for nei in neighbors(combo): 
                    if nei not in visited and nei not in dead: 
                        q.append(nei)
                        visited.add(nei)
            moves += 1

        return -1        