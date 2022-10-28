def nap(arr,n,target):
    
    dp=sorted(arr)
    dp=[[-float('inf ')]*(target+1) for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,target+1):
            # if i==0 or j==0:dp[i][j]=0
            if arr[i-1]>j:dp[i][j]=dp[i-1][j]
            elif arr[i-1]==j:dp[i][j]=1
            else: dp[i][j]=max(1+dp[i][j-arr[i-1]],dp[i-1][j])
    for j in range(target,-1,-1):
        if dp[n][j]!=-float('inf'):return dp[i][j]
    return 0
# print(nap([3,7,9],3,11))
# 3 11
# 3 7 9
l=list(map(int,input().split()))
target=l.pop(0)

print(nap(l,3,target))