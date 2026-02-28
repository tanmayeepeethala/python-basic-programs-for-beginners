n=int(input("Enter range:"))
sum=8
k=5
print(sum,end=",")
sum=sum+k
for i in range(1,n):
	if n-1==i:
		print(sum)
	else:
		print(sum,end=",")
	sum=sum+k+i
