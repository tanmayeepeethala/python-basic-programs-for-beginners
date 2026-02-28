n=int(input("Enter range:"))
sum=0
for i in range(n):
	if n-1==i:
		print(sum+i+2)
	else:
		sum=sum+i+2
		print(sum,end=",")