m=int(input("Enter m value:"))
n=int(input("Enter n value:"))
while n>0:
	rem=m%n
	m=n
	n=rem
print(m)