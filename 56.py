n=int(input("Enter a number:"))
num=n
sum=0
while n>0:
	rem=n%10
	sum=sum+rem**3
	n=n//10
if sum==num:
	print("Armstrong number")
else:
	print("Not an Armstrong number")