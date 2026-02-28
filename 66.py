n=int(input("Enter range:"))
sum=0
for i in range(1,n+1):
	if i==n:
		print(sum+i)
	else:
		sum=sum+i
		print(sum,end=",")