// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        nn=n
        n=2*n-1
        q=[['(',1,0]]
        while n:

            tem=[]
            while q:
                s,a,b=q.pop()
                # if a==n and b==n:return q
                if a==nn:
                     tem.append([s+')',a,b+1])
                elif a==b:
                     tem.append([s+'(',a+1,b])
                else:
                    tem.append([s+')',a,b+1])
                    tem.append([s+'(',a+1,b])
            q=tem.copy()
            n-=1
        return list(set([h for h,_,_ in q]))
            
        # i=1
        # l=set()
        # for i in range (1,n+1):
        #     s=''
        #     for j in range(i,n+1,i):
        #        s+=(i*'('+i*')')
        #     m=(((n-j))*'('+((n-j))*')')
        #     l.add(m+s)
        #     l.add(s+m)
        # return list(l)
# print(generateParenthesis(3))
#         i=1
#         l=[]
#         for i in range (1,n+1):
#             s=''
#             for j in range(i,n+1,i):
#                s+=(i*'('+i*')')
#             s+=(((n+1)%j)*'('+((n+1)%j)*')')
#             l.append(s)
#         return l
        