def computeXOR(n) :
 
    # if n is multiple of 4
    if n % 4 == 0 :
        return n
 
    # If n % 4 gives remainder 1
    if n % 4 == 1 :
        return 1
 
    # If n%4 gives remainder 2
    if n % 4 == 2 :
        return n + 1
 
    # If n%4 gives remainder 3
    return 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    xor = computeXOR(a-1)
    if xor == b: print(a)
    elif xor ^ b == a: print(a+2)
    else: print(a+1)