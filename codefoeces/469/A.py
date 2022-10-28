n=int(input())
l=list(map(int,input().split()))
p=l[0];l=l[1:]
# l=set(l)
m=list(map(int,input().split()))
q=m[0];m=m[1:]
# m=set(m)

tem=len(set(l+m))
# print(set(l))
# print(set(m))
# p=True

# for i in range(1,n+1):
#     if i in l or i in m:
#       pass
#     else:
#       p=False
if tem==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')