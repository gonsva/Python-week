msg=input("Enter any message: ")
word=0
i=0

def change(message):
	while i<len(msg):
		if msg[i]==" ":
			word=word+1

		if ord(msg)>=65 and ord(msg)<=90:
			print(chr(ord(msg)+32))
		else:
			if ord (msg)>=97 and ord(msg)<=122:
				print(chr(ord(msg)-32))
			else:
				if ord(msg)>=48 and ord(msg)<=57:
					print(*2)