n=int(input("Enter range:"))
m=2
for i in range(n):
	if i==n-1:
		print(m*(3**i))
	else:
		print(m*(3**i),end=",")