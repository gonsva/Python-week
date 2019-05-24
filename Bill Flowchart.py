pro=input ("Enter Product Name:")
pri=input ("Enter Product Price:")
qty=input ("Enter QTY:")
amt=float(pri)*int(qty)
vat=amt*15/100
total=amt+vat
print ("Bill")
print ("Product:",pro)
print ("Amount:",amt)
print ("VAT:",vat)
print ("Total:",total)