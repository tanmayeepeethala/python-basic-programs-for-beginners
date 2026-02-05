s=input("Enter a string:")
n=int(input("Enter index:"))
k=input("replaced character:")
str=""
l=len(s)
for i in range(l):
	if (i+1)%n==0:
		str=str+k
	else:
		str=str+s[i]
print(str)