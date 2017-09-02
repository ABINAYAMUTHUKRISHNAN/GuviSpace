num1=int(input("Enter the first Number:"))
num2=int(input("Enter the second Number:"))
num3=int(input("Enter the third Number:"))
val=" is Greater"
if num1>num2 and num1>num3:
	print(str(num1)+val)
elif num2>num3:
	print(str(num2)+val)
else:
	print(str(num3)+val)

