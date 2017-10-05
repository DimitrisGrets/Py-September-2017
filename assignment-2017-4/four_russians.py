import sys

def my_log(base,x):
	cons = 1
	counter = 0
	while(cons*base<x):
		cons *= base
		counter += 1
	return counter

def RowFromBottom(List,k):
	return (List[len(List)-k])

def sum_rows( templist1,templist2 , n):
	sumlist = []
	for i in range(n):
		sumlist.append(templist1[i] or templist2[i])
	return (sumlist)

def InitWithZeros(n):
	list = []
	for i in range(n):
		list.append(0)
	return list

def Num(list,n):
	sum = 0
	for i in range(n):
		sum = sum + list[i]*(2**(n-1-i))

	return sum

def fix_columns(List , Dlgn):
	n = len(List[0])
	nA = len(List[0])
	while (nA/Dlgn != int(nA/Dlgn)):  # filling A with 0 columns
		for i in range(n):
			List[i].append(0)
		nA = len(List[0])
	return List

def fix_rows(List , Dlgn , n):
	nB = len(List)  # listB lenght by line
	while (nB / Dlgn != int(nB / Dlgn)):  # filling B with 0 lines
		templist = []
		for i in range(n):
			templist.append(0)
		List.append(templist)
		nB = len(List)
	return List

def makeNBarray(n,templist):
	nbList = []
	for i in range(n):
		nbList.append(InitWithZeros(n))
	for i in range(0, len(templist), 2):  # pinakas gitniasis
		row = templist[i]
		column = templist[i + 1]
		nbList[row][column] = 1

	for i in range(len(nbList)):  # gemizoume tin diagonio tou pinaka gitniasis
		nbList[i][i] = 1
	return nbList

def russians4(ListA , ListB , Dlgn):
	nB = len(ListB)
	nA = len(ListA[0])
	n=len(ListA)
	no_subarrays = int(nB/Dlgn)
	ListC = []
	for i in range(n):
		ListC.append(InitWithZeros(n))
	for i in range(no_subarrays):		#ipopinakes
		rs = []
		bp = 1
		k = 0
		rs.append(InitWithZeros(n))
		nRS = 2**Dlgn
		Bi = []
		Ai = []
		for j in range(i*Dlgn,(i+1)*Dlgn,1):
			Bi.append(ListB[j])
		for j in range(n):
			templist = []
			for k in range(Dlgn):
				templist.append(ListA[j][(i*Dlgn)+k])
			Ai.append(templist)
		k=0
		j=1

		while (j <= nRS):
			rs.append(sum_rows(rs[j-(2**k)],RowFromBottom(Bi,k+1),n))

			if (bp == 1):
				bp = j + 1
				k += 1
			else:
				bp -= 1
			j += 1
		Ci = []
		for j in range(n):
			Ci.append(rs[Num(Ai[j], Dlgn)])
		for k in range(len(ListC)):
			ListC[k]=sum_rows(ListC[k],Ci[k],n)

	return ListC


print("four russians")

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if (len(sys.argv) == 3): 			#2 arrays given
	file = open(sys.argv[1], "r")
	ListA =[]
	for line in file:
		templist =[]
		for x in line:
			if (x=="0" or x=="1"):		# getrid of ","
				templist.append(int(x))
		if line:
			ListA.append(templist)
	file.close()

	file = open(sys.argv[2], "r")
	ListB =[]
	for line in file:
		templist =[]
		for x in line:
			if (x=="0" or x=="1"):
				templist.append(int(x))
		if line:
			ListB.append(templist)
	file.close()


	nA = len(ListA[0]) #listA length by column
	nB = len(ListB) # listB lenght by line
	n = len(ListA[0])

	Dlgn = my_log(2,n)

	ListA = fix_columns(ListA,Dlgn)
	ListB = fix_rows(ListB,Dlgn,n)

	ListC = russians4(ListA , ListB , Dlgn)

	print("Output:")
	for i in range(len(ListC)):
		for j in range(len(ListC[0])):
			print(ListC[i][j],",",end="",sep="")
		print("\n")

elif(len(sys.argv) == 2):		#graph given
	print("four russians graph")
	file = open(sys.argv[1], "r")
	templist = []
	for line in file:
		for x in line:
			if( x!= " " and x!="\n"):
				templist.append(int(x))
	file.close()

	n = int(max(templist)) + 1 #number of nodes (arithmimenoi apo to 0)

	Dlgn = my_log(2, n)

	for i in range(n):
		if(i==0):
			temp1 = fix_columns(makeNBarray(n,templist),Dlgn)
			temp2 = fix_rows(makeNBarray(n,templist),Dlgn,n)
			G = russians4(temp1,temp2,Dlgn)
		else:
			G = russians4(fix_columns(G,Dlgn),fix_rows(makeNBarray(n,templist),Dlgn,n),Dlgn)
	print("Output:")
	for i in range(n):
		for j in range(n):
			if(G[i][j]!=0):
				print(i,j)
else:
	print("wrong input")

