// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
            def sm(m): return sum([int(i) for i in list(str(m))])
    
            need=0
            div=1
            while sm(n)>target:
                tmp=math.ceil(n/(10**div)) *(10**div)
                need+=tmp-n
                n=tmp
                div+=1
            return need 