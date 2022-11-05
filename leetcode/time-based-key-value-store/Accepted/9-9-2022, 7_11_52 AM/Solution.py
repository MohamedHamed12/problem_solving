// https://leetcode.com/problems/time-based-key-value-store

class TimeMap:

    def __init__(self):
        self.d=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        l=self.d[key]
        tmp=bisect_right(l,[timestamp])
        if tmp>=len(l) or l[tmp][0]!=timestamp:tmp-=1
        if tmp==-1:return ''
        return l[tmp][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)