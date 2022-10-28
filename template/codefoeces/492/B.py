from  sys import maxsize, stdin
#fun to solve the problem
def solve(a,b,l):
   l=sorted(l,)
   t1=l[0]
   tot=0
   for i in range(1,a):
      tot=max(tot,l[i]-l[i-1])
   
   t2=(b-l[-1])
   m=max(t1,t2,float (tot/2))
   print(f"{m:0.10f}")

    

#fun to test the solution of the problem
def test(problem):
    pass
    


#input number of inputs
a,b=(int(i) for i in stdin.readline().split())
l=list(int(i) for i in stdin.readline().split())
solve(a,b,l)