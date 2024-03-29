n, m = int(input()) + 1, 1000000007
q, p = [[] for i in range(n)], [[] for i in range(n)]
w = [0] + list(map(int, input().split()))
for i in range(int(input())):
    u, v = map(int, input().split())
    p[u].append(v)
    q[v].append(u)
r = set(i for i in range(1, n) if not p[i] or not q[i])
s, t = 0, 1
while r:
    i = r.pop()
    s += w[i]
    for j in p[i]:
        q[j].remove(i)
        if not q[j]: r.add(j)
    for j in q[i]:
        p[j].remove(i)
        if not p[j]: r.add(j)
r = set(i for i in range(1, n) if p[i] and q[i])
while r:
    i = r.pop()
    h = p[i]
    d, k = w[i], 1
    while h:
        i = h.pop()
        if not i in r: continue
        r.remove(i)
        h += p[i]
        if w[i] == d: k += 1
        elif w[i] < d: d, k = w[i], 1
    s += d
    t = (t * k) % m
print(s,t)