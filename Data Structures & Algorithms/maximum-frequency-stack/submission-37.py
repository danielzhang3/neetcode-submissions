class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.stack = defaultdict(list)
        self.maxf = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f

        if f > self.maxf: 
            self.maxf = f
        self.stack[f].append(val)

    def pop(self) -> int:
        val = self.stack[self.maxf].pop()
        self.freq[val] -= 1

        if not self.stack[self.maxf]: 
            self.maxf -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()