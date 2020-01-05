def F2(L,n):
	R = [1]*n
	for i in range(1,n):
		for j in range(0,i):
			if L[i]>L[j] and R[j]+1 > R[i]:
				R[i] = R[j]+1
	for i in range(1,n):
		for j in range(0,i):
			if L[i]<L[j] and R[j]+1 > R[i]:
				R[i] = R[j]+1
	maximum = 0
	for e in R:
		maximum = max(maximum,e)
	print(n-maximum)

while True:
	L = eval(input('heights list:'))
	n = len(L)
	F2(L,n)