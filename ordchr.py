Alpha=input("Enter any Character: ")

if ord(Alpha)>=65 and ord(Alpha)<=90:
	print("UPPERCASE")
else:
	if ord (Alpha)>=97 and ord(Alpha)<=122:
		print("lowercase")
	else:
		if ord(Alpha)>=48 and ord(Alpha)<=57:
			print("Digits")
		else:
			print("Other Character")