
def solve():
    tot=0
    i=2
    while True:
        print('?',1,i)
        x=int(input())
        print('?',i,1)
        y=int(input())
        if x!=y:tot=x+y;break
        if x==-1 or y==-1:tot=i-1;break
        i+=1
    print("!",tot)
if __name__ == "__main__":
    solve()