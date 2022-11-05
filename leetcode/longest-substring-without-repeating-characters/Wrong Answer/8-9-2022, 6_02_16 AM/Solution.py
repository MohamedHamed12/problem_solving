// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=j=0
        mx=0
        st=set()
        n=len(s)
        while i<=n-1:
            if s[i] in st:
                while j<=n-1:
                    if s[j]==s[i]:
                        j+=1
                        mx=max(mx,i-j+1)
                        break
                    j+=1
                
            st.add(s[i])
            i+=1
        mx=max(mx,i-j)
        return mx
    
    
#         i=0
#         mx=0
#         st=[]
#         l=[]
#         n=len(s)
#         while i<=n-1:
#             j=i
#             while j<=n-1:
#                 if s[j] in st:
#                     i=j
#                     st.clear()
#                     break
#                 st.append(s[j])
#                 mx=max(mx,len(st))
#                 j+=1
#                 i=j
#         return mx