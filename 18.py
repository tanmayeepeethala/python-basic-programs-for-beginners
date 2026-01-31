ch=input("Enter a character: ")
v="aeiouAEIOU"
n="0,1,2,3,4,5,6,7,8,9"
if ch in v:
	print("VOWEL")
elif ch>='A' and ch<='Z' or ch>='a' and ch<='z':
	print("CONSONANT")
elif ch in n:
	print("DIGIT")
else:
	print("SPECIAL CHARACTER")