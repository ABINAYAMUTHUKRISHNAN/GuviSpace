num1=int(input("Enter the first number:"))
num2=int(input("Enter the sec number:"))
list1=[]
for i in range(num1,num2+1):
 j=i
 k=i
 count=0
 arm_num=0
 while(i!=0):
    rem=i%10
    count+=1
    i/=10
 while(j!=0):
    rem1=i%10
    arm_num+=rem1**count
    j/=10
 if arm_num==k:
    list1+=[k]
if len(list1)>0:
  print(list1)
else: 
  print("No Armstrong Number found")
