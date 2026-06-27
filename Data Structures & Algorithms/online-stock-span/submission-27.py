class StockSpanner:

    def __init__(self):
        self.stockspan = []

    def next(self, price: int) -> int:
        span = 1
        while self.stockspan and self.stockspan[-1][0] <= price: 
            span += self.stockspan.pop()[1]
        
        self.stockspan.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)