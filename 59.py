l=list(map(int,input("Enter elements:").split()))
sl=sorted(l)
d=min(sl[i+1]-sl[i] for i in range(len(sl)-1))
for i in range(len(sl)-1):
	if sl[i+1]-sl[i]==d:
		continue
	else:
		a=sl[i]+d
		print(a)
