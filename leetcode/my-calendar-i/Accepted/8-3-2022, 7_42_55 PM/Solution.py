// https://leetcode.com/problems/my-calendar-i

class MyCalendar:

    def __init__(self):
        self.c=[]
        

    def book(self, start: int, end: int) -> bool:
            ind=bisect_right(self.c,[start,end])
            if ind!=0 and self.c[ind-1][1]>start:return False
            if ind!=len(self.c) and self.c[ind][0]<end:return False
            insort(self.c,[start,end])
            return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)