// https://leetcode.com/problems/find-all-good-indices

class Solution:
    def goodIndices(self, l: List[int], k: int) -> List[int]:
        tmp=1
        same=[]
        tot=[]
        n=len(l)
        i=1
        while i<n:
            if l[i]<l[i-1]:tmp+=1;same=[]
            elif l[i]==l[i-1] and tmp<k:tmp+=1;same=[]
            elif  l[i]==l[i-1] :same.append(i)
            elif l[i]>l[i-1] :
                for j in range(i,n):
                    if l[j]>=l[j-1]:continue
                    else:break
                if j-i+1>=k:
                    if tmp>=k:tot+=same
                    else:tot+=max(0,(tmp+len(same))-k)*[same[0]]
                tmp=0;same=[]


                i=max(i,j-1)

                
          
            i+=1
        return tot