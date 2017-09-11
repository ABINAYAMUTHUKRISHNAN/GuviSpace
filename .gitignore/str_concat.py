
str1=input("Enter the first string:")
str2=input("Enter the second string:")
var=''
for i in range(0,len(str1)):
  if str1[i].isalpha():
    var+=str1[i]
  else:
    print("Invalid entry")
    break
for j in range(0,len(str2)):
  if str2[j].isalpha():
    var+=str2[j]
  else:
    print("Invalid entry")
    break
if len(var)==len(str1)+len(str2):
  print(var)
