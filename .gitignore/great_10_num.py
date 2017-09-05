num=[]
for i in range(0,10):
  num+=[int(input())]
great=0
for i in num:
  if i>great:
    great=i
print(great)
