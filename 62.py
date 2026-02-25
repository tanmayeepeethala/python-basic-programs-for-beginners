l=list(map(int,input("Enter elements:").split()))
lst=[]
for i in l:
	if i in lst:
		continue
	else:
		lst.append(i)
for i in lst:
	if i in l:
		l.remove(i)
ls=set(l)
for i in ls:
	print(i)