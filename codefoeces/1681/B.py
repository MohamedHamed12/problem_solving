for i in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	n2=int(input())
	l2=list(map(int,input().split()))
	print(l[sum(l2)%n])