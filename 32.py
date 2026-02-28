s=input("Enter a string:")
st=""
for ch1 in s: 
	if ch1 not in st:
		c=0
		for ch2 in s:
			if ch1==ch2:
				c=c+1
		print(ch1,":",c)
		st=st+ch1