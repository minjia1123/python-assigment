def Create_dict():
	n = int(input('please input the amount of nodes:'))#v0 - vn-1
	N = []
	V = [0]*n
	mydict = {};P = {};Tra = {}
	for i in range(n):
		N.append('v'+str(i))
		V[i] = int(input(N[i]+" time:"))
		if N[i] not in mydict:
			mydict[N[i]] = {'time':V[i],'pre':[],'end':[]}
			P[N[i]] = 0
			Tra[N[i]] = '-1'
	print("please input edges,like 0 1,ending with '-1 -1':")
	pre,end = 0,0
	while(pre != -1):
		pre,end = [eval(x) for x in input().split()]
		if pre != -1:
			mydict[N[end]]['pre'].append(N[pre])
			mydict[N[pre]]['end'].append(N[end])
	print(mydict)
	return mydict,P,Tra

def LP(mydict,P,Tra):
	s = []
	end = []
	for key in mydict:
		if mydict[key]['pre'] == []: 
			s.append(key)
			P[key] = mydict[key]['time']
		if mydict[key]['end'] == []:
			end.append(key)
	for e in s:
		for x in mydict[e]['end']:
			if P[e]+mydict[x]['time'] > P[x]:
				P[x] = P[e] + mydict[x]['time']
				Tra[x] = e 
			mydict[x]['pre'].remove(e)
			if mydict[x]['pre'] == []: s.append(x)
	L = 0; TTra = []; strr = ""
	for e in end:
		if P[e] > L:
			L = P[e]
			lp_tra = e
	while lp_tra!='-1':
		TTra.append(lp_tra)
		lp_tra = Tra[lp_tra]
	for i in range(len(TTra)-1,-1,-1):
		if i != 0: strr = strr + TTra[i] + "->"
		else: strr += TTra[i]
	print(strr)
	print(L) 

#main function
while True:
	mydict,P,Tra = Create_dict()
	LP(mydict,P,Tra)
