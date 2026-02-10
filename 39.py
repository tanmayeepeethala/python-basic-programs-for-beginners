lst=list(map(int,input("Enter elements into the list:").split(",")))
for i in range(len(lst)):
	for j in range(len(lst)):
		if lst[i] < lst[j]:
			temp=lst[i]
			lst[i]=lst[j]
			lst[j]=temp
print(lst)