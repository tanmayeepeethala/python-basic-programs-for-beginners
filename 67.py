n=int(input("Enter range:"))
sum=0
for i in range(n):
	sum=sum+i+2
	if n-1==i:
		print(sum)
	else:
		print(sum,end=",")