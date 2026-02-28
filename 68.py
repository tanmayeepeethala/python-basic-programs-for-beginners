n=int(input("Enter range:"))
sum=1
print(sum,end=",")
for i in range(2,n+1):
	if i%2==1:
		sum=sum*3
	else:
		sum=sum+1
	if i==n:
		print(sum)
	
	else:
		print(sum,end=",")