num=int(input("Enter the number:"))
if num>=1:
  for i in range(1,11):
    mul=num*i
    print(("%d*%d=%d")%(num,i,mul))
else:
  print("0")
