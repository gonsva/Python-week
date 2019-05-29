def change(message):
	i=0
	newmessage=""

	while i<len(message):
		ASCII= ord(message[i])
		if ASCII>=65 and ASCII<=90:
			newmessage += chr(ASCII+32)
		else:
			if ASCII>=97 and ASCII<=122:
				newmessage+= chr(ASCII-32)
			else:
				if ASCII>=48 and ASCII<=57:
					newmessage +=str(int(chr(ASCII))*2)
				else:
					newmessage+=chr(ASCII)
		i+=1
	return newmessage

message=input("Enter any message")
print (change(message))


