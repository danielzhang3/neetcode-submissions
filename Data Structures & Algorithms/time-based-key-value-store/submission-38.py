class TimeMap:

    def __init__(self):
        self.timeMap = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap: 
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap: 
            return ""
        
        values = self.timeMap[key]
        l, r = 0, len(values) - 1
        res = ""

        while l <= r: 
            mid = (l + r) // 2
            if values[mid][0] <= timestamp: 
                res = values[mid][1]
                l = mid + 1
            else: 
                r = mid - 1
        
        return res
        
