num=int(input("Enter the number:"))
sum=1
if num>=1:
  for i in range(1,num+1):
    sum*=i
  print(sum)
else:
  print("0")
