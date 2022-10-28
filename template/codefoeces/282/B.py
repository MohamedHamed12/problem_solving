tx=0
ty=0
s=""
for i in range(int(input())):
	
	
	x,y=map(int,input().split())
	if abs(tx+x -ty)<=500:
		s+="A"
		tx+=x
	else:
		s+="G"
		ty+=y
print(s)