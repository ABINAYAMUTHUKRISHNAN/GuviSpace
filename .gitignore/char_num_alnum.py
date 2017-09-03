var=input()
alphacount=0
numcount=0
alnumcount=0
for i in var:
  if i.isalpha():
    alphacount+=1
  elif i.isdigit():
    numcount+=1
  elif i.isalnum():
    alnumcount+=1
  else:
    print("INVALID")
print(alphacount)
print(numcount)
print(alnumcount)
