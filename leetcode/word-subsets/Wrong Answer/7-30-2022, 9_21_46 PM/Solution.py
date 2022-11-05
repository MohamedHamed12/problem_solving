// https://leetcode.com/problems/word-subsets

class Solution:
    def wordSubsets(self, w1: List[str], w2: List[str]) -> List[str]:
        def check(w1,w2):
            w1=list(w1);w2=list(w2)
            for i in w2:
               try:
                  w1.remove(i)
               except:
                return False
            return True 
        tot=[]
        w2="".join(w2)
        for i in w1:
            if check(i,w2):tot.append(i)
        return tot
            
        