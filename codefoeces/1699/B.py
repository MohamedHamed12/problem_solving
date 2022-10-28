from  sys import stdin
#fun to solve the problem
def solve(a,b):
    t1=1;t2=0
    teml=[];l=[]
    bp=[]
    for i in range(0,b//2):
        teml.append(t1)
        teml.append(t2)
        bp.append(t2)
        bp.append(t1)
        t1,t2=t2,t1
    for i in range(a//2):
        if i%2==0:
            l.append(teml)
            l.append(bp)

        else:
            l.append(bp)
            l.append(teml)



        
    for i in l:
            print(*i)

    


for i in range(int(input())):
    a,b=(int(i) for i in stdin.readline().split())
    solve(a,b)

    
 
# t=[1 ,2 ,3]
# print(t[::-1])