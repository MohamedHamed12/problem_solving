// https://leetcode.com/problems/count-days-spent-together

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
            a1,a2=min(leaveAlice,leaveBob).split("-")
            b1,b2=max(arriveAlice,arriveBob).split("-")
            d1=datetime.datetime(2022, int(a1), int(a2))
            d2=datetime.datetime(2022, int(b1), int(b2))
            return (d1-d2).days+1