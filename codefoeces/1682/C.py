import collections
import math 


for i in range(int(input())):
	n=n=int(input())

	l=list(map(int,input().split()))
	l2=set(l)
	n2=len(l2)
	tot=0
	tot2=0
	if n2>1:
		
		dic=collections.Counter(l)
		for h  in dic:
			if dic[h]>1:
				tot2+=1
			elif dic[h]==1:
				tot+=1
		print(tot2+math.ceil(tot/2))


 

	else:
		print(1)

# dic=collections.Counter(list(map(int,input().split())))
# print(dic)