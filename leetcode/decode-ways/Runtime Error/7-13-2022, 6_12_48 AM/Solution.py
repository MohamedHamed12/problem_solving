// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
      n=len(s)
      tot=[0]*n
      if s[0]=='0':return 0
      if n==1 :return 1
       
      if s[-1] == '0':tot[-1]=0
      else:tot[-1]=1
      if s[-2] == '0'or int(s[-2:])>26 or :tot[-2]=0+tot[-1]
      else:tot[-2]=tot[-1]+1
      for i in range(n-3,-1,-1):
             if  s[i+1]=='0' and  int(s[i])>2:return 0
             if s[i:i+2]=='00':return 0
             if int(s[i:i+2])>26 or s[i]=='0' or s[i+1]=='0'or s[i+2]=='0':tot[i]=tot[i+1]
             else:tot[i]=tot[i+1]+tot[i+2]
      return tot[0]
        # s=list(s);tot=1
        # if s[0]=='0':return 0
        # if len(s)==1:return 1
        # for i in range(len(s)-2):
        #   if int("".join(s[i:i+2]))<=26 and ('0' not in s[i:i+2] )and s[i+2]!='0':tot*=2
        #   if s[i+1]=='0':i+=1
        # if int("".join(s[-2:]))<=26 and ('0' not in s[-2:] ):tot+=1
        # return tot