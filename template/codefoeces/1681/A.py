def getvalue(l1,l2):
	m1=max(l1)
	m2=max(l2)
	if m1>=m2:
		return 1
	else :
		return 2
for i in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	n2=int(input())
	l2=list(map(int,input().split()))
	if getvalue(l,l2)==1:
		print ("Alice")
	else:
		print("Bob")
	if getvalue(l2,l)==1:
		print("Bob")
		
	else:
		print ("Alice")