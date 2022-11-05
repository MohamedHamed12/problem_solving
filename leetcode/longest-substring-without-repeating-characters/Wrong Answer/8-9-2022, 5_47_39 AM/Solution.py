// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        mx=0
        st=set()
        n=len(s)
        while i<n-1:
            j=i
            while j<=n-1:
                if s[j] in st:
                    i=j
                    st.clear()
                    break
                st.add(s[j])
                mx=max(mx,len(st))
                j+=1
        return mx