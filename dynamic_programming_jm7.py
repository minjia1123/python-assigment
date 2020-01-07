# F(x0,y0,xn,yn) = 
# 1. 0, 在(x0,y0,xn,yn)区域内没有点
# 2. min(...,min(F(x0,yk,xn,yn)+F(x0,y0,xn,yk)+xn-x0,F(x0,y0,xk,yn)+F(xk,y0,xn,yn)+yn-y0),...), 在(x0,y0,xn,yn)区域内存在点，k表示点序号
#
# 由于各个可能交点人为计算十分复杂，很难直接用四维数列存储区域，因此使用深搜的办法找到所有的可能区域，然后实现上述函数操作。
# 顺序的记录用一个Tra,记录每一个区域的分割情况（两个新矩阵和分割线段），最后递归输出分割步骤
def F(x0,y0,xn,yn):
	if (x0,y0,xn,yn) in mydict:
		return mydict[x0,y0,xn,yn]
	mydict[x0,y0,xn,yn] = 0
	for e in N:
		if x0<e[0]<xn and y0<e[1]<yn:
			m = F(x0,e[1],xn,yn) + F(x0,y0,xn,e[1]) + xn - x0
			n = F(x0,y0,e[0],yn) + F(e[0],y0,xn,yn) + yn - y0			
			if mydict[x0,y0,xn,yn]== 0 or mydict[x0,y0,xn,yn] > m:
				mydict[x0,y0,xn,yn] = m
				Tra[x0,y0,xn,yn] = [[x0,e[1],xn,yn],[e[0],e[1],0],[x0,y0,xn,e[1]]]
			if mydict[x0,y0,xn,yn]==0 or mydict[x0,y0,xn,yn] > n:
				mydict[x0,y0,xn,yn] = n
				Tra[x0,y0,xn,yn] = [[x0,y0,e[0],yn],[e[0],e[1],1],[e[0],y0,xn,yn]]
	return mydict[x0,y0,xn,yn]

def Draw(x0,y0,xn,yn):
	if (x0,y0,xn,yn) in Tra:
		print('('+str(Tra[x0,y0,xn,yn][1][0])+','+str(Tra[x0,y0,xn,yn][1][1])+')',end=':')
		if Tra[x0,y0,xn,yn][1][2] == 0:
			print('--')
		else:
			print('|')
		Draw(Tra[x0,y0,xn,yn][0][0],Tra[x0,y0,xn,yn][0][1],Tra[x0,y0,xn,yn][0][2],Tra[x0,y0,xn,yn][0][3])
		Draw(Tra[x0,y0,xn,yn][2][0],Tra[x0,y0,xn,yn][2][1],Tra[x0,y0,xn,yn][2][2],Tra[x0,y0,xn,yn][2][3])

while True:
	n = eval(input('nodes:'))
	l = len(n)
	N = [[0,0]] + n + [[100,80]]
	Tra = {}; mydict = {}
	print(F(0,0,100,80))
	Draw(0,0,100,80)