# C.Stripes
for t in range(int(input())):
    input()
    rows = []; B = 1
   
    for i in range(8):
        a = list(input())
        if len(a) == 8: rows.append(a);
    for row in rows:
        if row.count('R') == 8: print('R'); B = 0 ;break
    if B: print('B')


"""
# C. Stripes
result = []
k = int(input())
for time in range(k):
    rows = []; cols = []
    for i in range(10):
        a = list(input())
        if len(a) == 8: rows.append(a);
    for c in range(8):
        col = []
        for el in range(8):
            col.append(rows[el][c])
        cols.append(col)
    for row in rows:
        if row.count('B') == 8: result += 'B'; break  # print('B', 1); break
        elif row.count('R') == 8: result += 'R'; break  # print('R', 1); break
    for col in cols:
        if col.count('B') == 8: result += 'B'; break  # print('B'); break
        elif col.count('R') == 8: result += 'R'; break  # print('R'); break
print(*result, sep='\n')
"""