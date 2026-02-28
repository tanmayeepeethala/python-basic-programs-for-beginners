n=int(input("Enter range:"))
for i in range(1,n+1):
	if i==n:
		print(i*i)
	else:
		print(i*i,end=",")