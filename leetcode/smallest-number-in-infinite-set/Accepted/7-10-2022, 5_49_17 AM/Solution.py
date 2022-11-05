// https://leetcode.com/problems/smallest-number-in-infinite-set

import bisect
class SmallestInfiniteSet:

    def __init__(self):
        
        self.l=set()
        

    def popSmallest(self) -> int:
        i=1
        while i in self.l :
            i+=1
            
        self.l.add(i)
        return i
            
        # if len(self.l)>0:
        #     s=min(self.l)
        #     ind=self.l.index(s)
        #     return self.l.pop(ind)
        # return 0


    def addBack(self, num: int) -> None:
        # if num not in self.l: self.l.append(num)
          if num in self.l:self.l.remove(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)