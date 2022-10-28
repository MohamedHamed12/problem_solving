



for i in range(int(input())):
    nn = int(input())
    l = list(input())
    tot = []
    if nn==1:print(0);continue;
    for i in range(nn):
        if l[i] == 'L':
            tot.append(i)
        else:
            tot.append(nn-i-1)
    pp = []
    sm = sum(tot)
    lft = 0
    while lft < nn//2:

        if l[lft] == 'L':
            sm -= tot[lft]
            tot[lft] = nn-lft-1
            sm += tot[lft]
            pp.append(sm)
        
        if l[nn-lft-1] == 'R':
            sm -= tot[nn-lft-1]
            tot[nn-lft-1] = nn-lft-1
            sm += tot[nn-lft-1]
            pp.append(sm)
        lft += 1

    pp = sorted(pp)
    while len(pp) < nn:
         pp.append(sm)
     
    print(*pp)