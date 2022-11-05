// https://leetcode.com/problems/my-calendar-i

class MyCalendar:

    def __init__(self):
            self.calendar=[]
        

    def book(self, start: int, end: int) -> bool:
            ind=bisect_right(self.calendar,[start,end])
            if ind!=0 and self.calendar[ind-1][1]>start:return False
            if ind!=len(self.calendar) and self.calendar[ind][0]<end:return False
            self.calendar.insert(ind,[start,end])
            return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)