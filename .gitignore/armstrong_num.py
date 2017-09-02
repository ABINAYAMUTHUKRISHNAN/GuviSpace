num1=input("Enter the number:")
num2=num1
arm_num=0
length=len(num1)
while(int(num1)!=0):
    rem=int(num1)%10
    arm_num+=rem**length
    num1=int(num1)/10
if arm_num==int(num2):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
