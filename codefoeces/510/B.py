from  sys import stdin

def isvaild(x,y):
    if x>=0 and x<a and y>=0 and y<b:return True
    else: return False


def dfs(i,j):
    q=[[i,j]]
    indexs=[[1,0],[0,1],[-1,0],[0,-1]]
    while q:
        x,y=q.pop()
        for item in indexs:
            k,h=item
            if isvaild(x+k,y+h) and visit[x+k][y+h] and  l[x][y]==l[x+k][y+h]:
                if [x+k,y+h] in q:return True
                q.append([x+k,y+h])

        visit[x][y] =False 

def solve(a,b,l):
    for i in range(a):
        for j in range(b):
            if visit[i][j]:
                if dfs(i,j):return True 
    return False
    

# global a,b,l
a,b=list(int(i) for i in stdin.readline().split())
l=list(stdin.readline().strip() for i in range(a))  
visit=list([True]*b for i in range(a))

print("Yes") if solve(a,b,l) else print("No")