a,b=int(input())
if a<b:
  a,b=b,a
while b>0:
  c=b
  b=a%b
  a=c
print(a)
