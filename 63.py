l=list(map(int,input("Enter elements:").split()))
lst=[]
for i in l:
	if i not in lst:
		c=0
		for j in l:
			if i==j:
				c=c+1
		print(i,":",c)
		lst.append(i)