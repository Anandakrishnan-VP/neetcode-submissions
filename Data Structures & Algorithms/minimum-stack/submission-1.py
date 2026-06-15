class MinStack:

    def __init__(self):
       self.s = []
       self.s2=[]

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.s2:
            if self.s2[-1] >= val:
                self.s2.append(val)
        else:
            self.s2.append(val)
        

    def pop(self) -> None:
        if self.s[-1] == self.s2[-1]:
            self.s2.pop()
        self.s.pop()

    def top(self) -> int:
       return self.s[-1]
    
        

    def getMin(self) -> int:
            return self.s2[-1]

        
