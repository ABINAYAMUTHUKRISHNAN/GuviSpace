num1=input("Enter the first number:")
num2=input("Enter the sec number:")
arm_num=0
for i in range(int(num1),int(num2+1)):
 length=len(i)
 j=i
 while(int(i)!=0):
    rem=int(i)%10
    arm_num+=rem**length
    num1=int(i)/10
 if arm_num==j:
    list1+=[j]
 else:
    print("No Armstrong Numbers found")
