l1=[10,20,30,40]
a=int(input("A: "))
b=int(input("B: "))

temp=l1[a]
l1[a]=l1[b]
l1[b]=temp

print(l1)