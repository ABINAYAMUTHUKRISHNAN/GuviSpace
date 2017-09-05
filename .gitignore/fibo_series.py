num=int(input())
if num>=1:
 a=0
 b=1
 print(a)
 print(b)
 for i in range(2,num+1):
  c=a+b
  print(c)
  a=b
  b=c
else:
  print("INVALID")
  
