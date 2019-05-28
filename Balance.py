Bill=int(input ("Enter you bill: "))
Given =int(input ("Enter amount given: "))
Balance= Given-Bill
print("Balance:", Balance)
print ("----------")

fiftysowed = int(Balance / 50)
Balance = Balance % 50
if fiftysowed >= 1:
	print("50s:", fiftysowed)

twentysowed = int(Balance / 20)
Balance = Balance % 20
if twentysowed >= 1:
	print("20s:", twentysowed)

tensowed = int(Balance / 10)
Balance = Balance % 10
if tensowed >= 1:
	print("10s:", tensowed)

fivesowed = int(Balance / 5)
Balance = Balance % 5
if fivesowed >= 1:
	print("5s:", fivesowed)

twosowed = int(Balance / 2)
Balance = Balance % 2
if twosowed >= 1:
	print("2s:", twosowed)

onesowed = int(Balance / 1)
Balance = Balance % 1
if onesowed >= 1:
	print("1s:", onesowed)
print ("----------")

