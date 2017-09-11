
str1=input("Enter the first string:")
str2=input("Enter the second string:")
count=0
if len(str1)>len(str2):
 great=len(str1)
else:
  great=len(str2)
for i in range(0,great):
  if str1[i]==str2[i]:
   count+=1
  else:
    print("Disimilar")
    break
if len(str1)==count:
  print("Similar")
    
