// https://leetcode.com/problems/min-max-game

class Solution:
    def minMaxGame(self, nums) :
        
        # x1=[]
        # for i in nums:
        #     if i%2==0:
        if len(nums)==1:
            # print(nums[0])
            return nums[0]
        
        x1=[]
        tem=int(len(nums)/2)
        for i in range(tem) :
            
            if i%2==0:
                x1.append(min(nums[2*i],nums[2*i+1]))
            else:
                 x1.append(max(nums[2*i],nums[2*i+1]))
        return self.minMaxGame(x1)
# l=list(map(int,input().split()))
# l=[1,3,5,2,4,8,2,2]
# l=[3]
# while True:             # Loop continuously
inp = input() # Get the input
# if inp == "":       # If it is a blank line...
#     break 
l=list(int(i) for i in inp if  i.isdigit())
s=Solution()
print(s.minMaxGame(l))