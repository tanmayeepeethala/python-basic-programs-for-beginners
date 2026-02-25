l=list(map(int,input("Enter elements:").split()))
lst=[]
for i in l:
	if i in lst:
		continue
	else:
		lst.append(i)
print(lst)