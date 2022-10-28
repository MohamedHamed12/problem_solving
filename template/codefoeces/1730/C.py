

    



from collections import deque


for i in range(int(input())):
     ss = input()
     l = sorted(enumerate(list(ss)), key=lambda x: x[1])
     mx = 0
     t=deque()
     for i, j in l:
        if i < mx: j = str(min(int(j)+1, 9))
        t.append(j)
        mx = max(mx, i)
     t=sorted(t)
     kk="".join(t)
     print(kk)