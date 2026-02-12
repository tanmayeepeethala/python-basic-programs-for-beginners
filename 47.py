def large(n1,n2,n3):
	if n1>n2 and n1>n3:
		print(n1,"is largest among the numbers")
	elif n2>n3:
		print(n2,"is largest among the numbers")
	else:
		print(n3,"is largest among the numbers")
n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
n3=int(input("Enter number3:"))
large(n1,n2,n3)