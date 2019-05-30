try:
	no1=int(input("Enter first number"))
	no2=int(input("Enter second number"))
	result=no1/no2
	print("Result is ",result)

except ValueError:
	print("Please enter digits only")

except ZeroDivisionError:
	print("Cannot divide by zero")

except Exception:
	print("Something went wrong")

finally:
	print("ABC")