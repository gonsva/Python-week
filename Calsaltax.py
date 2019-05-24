name=input("Enter your name:")
sal=int(input("Enter your salary:"))
if sal>2000:
	tax=sal*25/100
else:
	tax=sal*15/100
netsal=sal-tax
print ("Name:",name)
print ("Salary:",sal)
print ("Net Salary:",netsal)