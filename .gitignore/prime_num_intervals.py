num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
list1=[]
if num1>=1:
  for i in range(num1,num2+1):
     for j in range(2,i):
         if i%j==0:
             break
     else:
        list1+=[i]
if len(list1)>0:
    print(list1)
else:
    print("No Prime Numbers found")
