# import collections
# import math 


# for i in range(int(input())):
# 	n=n=int(input())

# 	l=list(map(int,input().split()))
# 	l2=set(l)
# 	n2=len(l2)
# 	tot=0
# 	tot2=0
# 	if n2>1:
		
# 		dic=collections.Counter(l)
# 		for h  in dic:
# 			if dic[h]>1:
# 				tot2+=1
# 			elif dic[h]==1:
# 				tot+=1
# 		print(tot2+math.ceil(tot/2))


 

# 	else:
# 		print(1)

# # dic=collections.Counter(list(map(int,input().split())))
# # print(dic)

for i in range(int(input())):
	n=int(input())
	s=input()
	tot=1
	if n%2!=0:
		mid =int(n/2)
		b=True
		while b and mid<n-1:
			if s[mid]==s[mid+1]:
				tot+=1
				mid+=1
			else:
				b=False
		b=True
		mid =int(n/2)
		while b and mid>0:
			if s[mid]==s[mid-1]:
				tot+=1
				mid-=1
			else:
				b=False
		print(tot)
	else:
		mid =int(n/2)
		b=True
		while b and mid<n-1:
			if s[mid]==s[mid+1]:
				tot+=1
				mid+=1
			else:
				b=False
		b=True
		mid =int(n/2)
		while b and mid>0:
			if s[mid]==s[mid-1]:
				tot+=1
				mid-=1
			else:
				b=False
		print(tot)
 


# for i in range(n):
# 		tem=list(s)
# 		tem.pop(i)

# 		r=tem.copy()
# 		r.reverse()
# 		if tem==r:
# 			tot+=1