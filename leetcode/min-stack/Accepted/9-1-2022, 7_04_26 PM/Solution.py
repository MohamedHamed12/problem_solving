// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.lst=[]
        self.slst=[]
        self.m=float('inf')
        

    def push(self, val: int) -> None:
        self.lst.append(val)
        insort(self.slst,val)
        self.m=min(self.m,val)
        

    def pop(self) -> None:
        
        mm=self.lst.pop()
        del self.slst[bisect_right(self.slst,mm)-1]
        

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.slst[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()