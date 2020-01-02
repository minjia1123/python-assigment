def Create():
	mydict = {}#out:1, not out: 0, left: -1, right:1, up: -1, down: 1
	for x in range(n):
		for y in range(m):
			i = x*m*2 + 2*y
			mydict[i] = {'node':[x,y],'out':0,'lr':-1,'ud':0}
			mydict[i+1] = {'node':[x,y],'out':0,'lr':1,'ud':0}
			if M[x][y] == 0:
 				mydict[i]['ud'] = 1
 				mydict[i+1]['ud'] = -1
 				if x==0:
 					mydict[i+1]['out'] = 1
 				if x == n-1:
 					mydict[i]['out'] = 1
			else:
				mydict[i]['ud'] = -1
				mydict[i+1]['ud'] = 1
				if x == 0:
					mydict[i]['out'] = 1
				if x == n-1:
					mydict[i+1]['out'] = 1
			if y == 0:
				mydict[i]['out'] = 1
			if y == m-1:
				mydict[i+1]['out'] = 1
	return mydict

def DFS(v):
	visited[v] = 1
	global counter_node
	global counter_out
	counter_node += 1
	if mydict[v]['out'] == 1:
		counter_out += 1
	if mydict[v]['ud'] == -1:
		x = mydict[v]['node'][0] -1
		y = mydict[v]['node'][1]
		if x >=0:
			i = x*2*m + 2*y
			if mydict[i+1]['ud'] == 1:
				i += 1
			if visited[i] == 0: DFS(i)		
	if mydict[v]['lr'] == 1:
		if mydict[v]['node'][1] < m-1 and mydict[v+1]['lr'] == -1:
			if visited[v+1] == 0: DFS(v+1)
	if mydict[v]['ud'] == 1:
		x = mydict[v]['node'][0] + 1
		y = mydict[v]['node'][1]
		if x < n:
			i = x*2*m + 2*y
			if mydict[i+1]['ud'] == -1:
				i += 1
			if visited[i] == 0: DFS(i)	
	if mydict[v]['lr'] == -1:
		if mydict[v]['node'][1]>0 and mydict[v-1]['lr'] == 1:
			if visited[v-1] == 0: DFS(v-1)

print('please input n(raw) and m(col),seperated by space:')
n,m = [eval(x) for x in input().split()]
M = []
S = []#area
print('input n*m matrix line by line')
for x in range(n):
	L = eval(input('input line'+str(x+1)+':'))
	M.append(L)
mydict = Create()
visited = [0]*m*n*2
for e in range(m*n*2):
	counter_out = 0;counter_node = 0
	if visited[e] == 0:
		DFS(e)
		if counter_out == 0:
			S.append(int(1/2*counter_node))
ans = 0
for e in S:
	ans = max(ans,e)
print("closed areas:",S)
print("max area:",ans)