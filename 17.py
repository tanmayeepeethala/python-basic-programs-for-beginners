num=int(input("Enter a number:"))
c=0
while num>0:
	r=num%10
	c=c+1
	num=num//10
print(c)