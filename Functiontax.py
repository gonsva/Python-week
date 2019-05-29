def tax(salary):
	if salary>1500:
		t=salary*21/100
	else:
		t=salary*15/100
	return t

salary1=int(input("Enter your salary: "))
print ("Your tax", tax(salary1))
print("Net salary",(salary1-tax(salary1)))