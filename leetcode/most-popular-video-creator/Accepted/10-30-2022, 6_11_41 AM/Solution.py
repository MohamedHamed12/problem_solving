// https://leetcode.com/problems/most-popular-video-creator

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
            d=defaultdict(lambda :[0,"zzzzzzzzzzzzzzzz",0])

            for i,c in enumerate(creators):
                d[c][0]+=views[i]
                if d[c][2]<views[i]:
                    d[c][2]=views[i]
                    d[c][1]= ids[i]
                if d[c][2]==views[i]:
                    
               
                    d[c][1]=min(ids[i], d[c][1]) 
            d=sorted(d.items(),key=lambda x:x[1],reverse=True) 
            mx=d[0][1][0]       
            d=filter(lambda x:x[1][0]==mx,d)
            return sorted([[i,j[1]] for i ,j in d])

# creators = ["alice","bob","alice","chris"]
# ids = ["one","two","three","four"]
# views = [5,10,5,4]
# print(*mostPopularCreator(creators,ids,views))