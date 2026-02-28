n=int(input("Enter range:"))
sum=5
k=4
print(sum,end=",")
sum=sum+k
for i in range(1,n):
	if i==n-1:
		print(sum)
	else:
		print(sum,end=",")
	sum=sum+k+i