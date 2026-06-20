class FreqStack:

    def __init__(self):
        self.count = {}
        self.stacks = {}
        self.max = 0

    def push(self, val: int) -> None:
        freq = self.count.get(val,0) + 1
        self.count[val] = freq
        if self.max < freq:
            self.max = freq
            self.stacks[freq] =  []
        self.stacks[freq].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max].pop()
        self.count[res] -= 1
        if not self.stacks[self.max]:
            self.max -=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()