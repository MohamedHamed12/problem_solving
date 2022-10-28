l=[]

n=int(input())
for i in range(n):
    l.append(i)
if n%2!=0:
    print(*l)
    print(*l)

    for i in range(n):
        print((2*i)%n ,end=" ")
    print()
else:
    print(-1)





# m=[]
# for i in range(n):
#   tem=[]
#   for j in range(n):
#         tem.append((i+j)%n)
#   m.append(tem)
# for i in m:
#     print(*i)