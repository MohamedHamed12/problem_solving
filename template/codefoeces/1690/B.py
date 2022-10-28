def getans(l1, l2, n):
    max0=0
    tem=[]
    for i in range(n):
        if l1[i] < l2[i]:
            return "NO"
        else:
            if l2[i] == 0:
                max0=max(max0,l1[i])
            else:
                if len(tem)==0:
                   tem.append(l1[i]-l2[i])  
                else:
                    if tem[0]!=l1[i]-l2[i]:
                        return "NO"
    if  len(tem)>0 and  max0>tem[0]:
        return "NO"
    
    return "YES"
for i in range(int(input())):
    n = int(input())
    l1 = (list(map(int, input().split())))
    l2 = (list(map(int, input().split())))
    print(getans(l1, l2, n))