num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
list1=[]
for i in range(num1,num2+1):
    if i%2==0:
        list1+=[i]
print(list1)
