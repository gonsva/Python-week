
msg=input("Enter any message: ")
Q=input("What are you looking for: ")


if msg==Q:
	Q=msg.count(Q)
	
print ("There are", msg.count(Q), Q)