
num1=1
num2=1
num3=0

print (num1,num2," ", end = "")

for i in range(0,20):
	num3=num1+num2
	print(num3, " ", end = "")
	num1=num2
	num2=num3
