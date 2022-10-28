from  sys import stdin
#fun to solve the problem
def solve(n):
    i=1
    tot=1
    #while True
    while tot<n:
        tot=pow(4,i)
        i+=1
    print(i-1)

#fun to test the solution of the problem
def test(problem):
    pass
    


#input number of inputs
n=input()
solve(int(n,2))    
 

  

# print(int(input(),2))