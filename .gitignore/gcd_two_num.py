num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1<num2:
  n=num1
else:
  n=num2
for i in range(1,n):
  if num1%i==0 and num2%i==0:
    gcd=i
print(gcd)
