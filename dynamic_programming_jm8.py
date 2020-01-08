def find(u):
	vx[u] = 1
	for v in range(n):
		if vy[v]==0 and lx[u]+ly[v]== weight[u][v]:
			vy[v] = 1
			if match[v] == -1 or find(match[v]) == 1:
				match[v] = u
				return 1
	return 0

def KM():
	global vx,vy
	for i in range(n):
		for j in range(n):
			if lx[i]<weight[i][j]:
				lx[i] = weight[i][j]
	for u in range(n):
		while True:
			vx = [0]*n;vy = [0]*n
			if find(u)==1: break
			inc = -1
			for i in range(n):
				if vx[i] ==1:
					for j in range(n):
						if vy[j] == 0 and (inc==-1 or lx[i]+ly[j]-weight[i][j]<inc):
							inc = lx[i]+ly[j]-weight[i][j]
			for i in range(n):
				if vx[i]==1:
					lx[i] -= inc
				if vy[i]==1:
					ly[i] += inc
	sum = 0
	for j in range(n):
		if match[j] > -1:
			sum += weight[match[j]][j]
	return sum

#main
while True:
	n = int(input('please input n:'))
	weight = [[0]*n for i in range(n)]
	for i in range(n):
		weight[i] = [eval(x) for x in input().split()]
	lx = [0]*n; ly = [0]*n
	vx = [0]*n; vy = [0]*n
	match = [-1]*n
	print(KM())