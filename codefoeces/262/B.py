from  sys import stdin
def test(problem):
    pass
def solve(a,b,l):
    tot=0;m=abs(l[0])
    for i in range(a):
        # if b==0:break
       
        if l[i]<0 and b>0:
            l[i]*=-1
            b-=1
        tot+=l[i]
        m=min(abs(l[i]),m)
    if b>0 :
        if b%2!=0:tot-=m*2
        
    
    return tot  
    


a,b=list(int(i) for i in stdin.readline().split())
l=list(int(i) for i in stdin.readline().split())
    
print( solve(a,b,l))

# tot=0

# a="257 320 676 1136 2068 2505 2639 4225 4951 5786 7677 7697 7851 8337 8429 8469 9343"
# for i in a.split():
#   tot+=int(i)
# print (tot)