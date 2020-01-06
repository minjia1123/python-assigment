def matrix_chain_order(P):
	length = len(P)-1
	M = [[-1 for i in range(length)] for j in range(length)]
	S = [[0]*length for j in range(length)]
	for i in range(length):
		for j in range(length):
			if i == j: M[i][j] = 0
	for l in range(2,length+1):
		for i in range(length-l+1):
			j = i + l - 1
			for k in range(i,j):
				if M[i][j] == -1 or M[i][j] > M[i][k] + M[k+1][j] + P[i]*P[k+1]*P[j+1]:
					M[i][j] = M[i][k] + M[k+1][j] + P[i]*P[k+1]*P[j+1]
					S[i][j] = k
	def order_string(S,i,j):
		if j == i+1:
			return "(A"+str(i)+"A"+str(j)+")"
		elif i == j:
			return "A"+str(i)
		else:
			a = S[i][j]
			return "("+order_string(S,i,a)+order_string(S,a+1,j)+")"
	print(order_string(S,0,length-1))
	print(M[0][length-1])

while True:
	P = [eval(x) for x in input('please input P:').split()]
	matrix_chain_order(P)
