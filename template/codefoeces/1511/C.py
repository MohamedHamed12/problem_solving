from collections import deque

a, b=map(int,input().split())
q1=deque(map(int,input().split()))
q2=deque(map(int,input().split()))

for i in q2 :
    
    print(q1.index(i)+1,end=" ")
    q1.remove(i)
    q1.appendleft(i)