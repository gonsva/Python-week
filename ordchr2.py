Alpha=input("Enter any alphabet: ")

if ord(Alpha)>=65 and ord(Alpha)<=90:
	print("----------------")
	print(chr(ord(Alpha)+32))
	print("----------------")
else:
	if ord (Alpha)>=97 and ord(Alpha)<=122:
		print("----------------")
		print(chr(ord(Alpha)-32))
		print("----------------")
	else:
		if ord(Alpha)>=48 and ord(Alpha)<=57:
			print("----------------")
			print("Digits")
			print("----------------")
		else:
			print("----------------")
			print("Other Character")
			print("----------------")