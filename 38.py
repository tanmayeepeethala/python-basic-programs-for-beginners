lst=list(map(int,input("Enter elements into list :").split(",")))
l=[]
for i in lst:
	if i in l:
		continue
	else:
		l.append(i)
print(l)