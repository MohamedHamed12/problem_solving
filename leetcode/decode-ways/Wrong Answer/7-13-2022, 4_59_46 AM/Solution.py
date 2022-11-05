// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        s=list(s);tot=1
        if s[0]=='0':return 0
        for i in range(len(s)-2):
          if int("".join(s[i:i+2]))<=26 and ('0' not in s[i:i+2] )and s[i+2]!='0':tot+=1
          if s[i+1]=='0':i+=1
        if int("".join(s[-2:]))<=26 and ('0' not in s[-2:] ):tot+=1
        return tot