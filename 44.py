def primecheck(n):
	c=0
	for i in range(2,n+1):
		if n%i==0:
			c=c+1
	if c==1:
		print("Prime")
	else:
		print("Not Prime")
n=int(input("Enter a number:"))
primecheck(n)