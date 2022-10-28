
t = int(input())
for _ in range(t):
    n = int(input())
    nums = []
    for i in range(2*n-1):
        a, b = map(int, input().split())
        nums.append([a,b, i+1])
    s=set()
    nums = sorted(nums)[::-1]
    vals=[]
    vals.append(nums[0][2])
    i=1

    while len(vals)<n:
        c=i
        if nums[i][1] <nums[i+1][1]:c+=1
        vals.append(nums[c][2])
        i += 2
        
    print("YES")
    print(*vals)