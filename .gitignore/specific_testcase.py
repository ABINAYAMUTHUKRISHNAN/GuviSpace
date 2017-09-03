sum=0
odd=0
for i in range(1,16):
  sum+=i
for i in range(15,46):
  if i%2!=0:
    odd+=i
print(sum)
print(odd)
