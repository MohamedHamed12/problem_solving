// https://leetcode.com/problems/word-subsets

class Solution:
    def wordSubsets(self, w1: List[str], w2: List[str]) -> List[str]:
        tot=[]
        d=defaultdict(int)
        for i in  (w2):
            c=Counter(i)
            for j in c:
                  if d[j] <c[j]:d[j] =c[j]
        for i in w1:
            c=Counter(i)
            b=True
            for j in d:
                
                  if d[j] >c[j]:
                        b=False
                        break
            if b:tot.append(i)

        return tot
#         def check(w1,w2):
#             w1=list(w1);w2=list(w2)
#             for i in w2:
#                try:
#                   w1.remove(i)
#                except:
#                 return False
#             return True 
#         tot=[]
#         # w2="".join(w2)
#         for i in w1:
#             b=True
#             for j in w2:
                
#               if not check(i,j):
#                   b=False
#                   break
#             if b:tot.append(i)
#         return tot
            
        