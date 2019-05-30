ones=["","One","Two", "Three", "Four", "Five", 
"Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
"Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
"Seventeen", "Eighteen", "Nineteen"]

tens=["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", 
"Seventy", "Eighty", "Ninty"]

num=int(input("Enter any number: "))
answer=""

if num>=1000 and num<=9000:
	answer+=ones[int(num/1000)]+ " Thousand "
	num=num%1000

if num>=100:
	answer+=ones[int(num/100)]+ " Hundred "
	num=num%100

if num>=20:
	answer+=tens[int(num/10)] + " "
	num=num%10

if num>=0 and num<=19:
	answer+=ones[num]

print(answer)