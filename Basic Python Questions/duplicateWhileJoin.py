a1=[1,5,10,20,40,80]
a2=[6,7,20,80,100]
a3=[3,4,15,20,30,70,80,120]

a11=set(a1)
a22=set(a2)
a33=set(a3)

print((a11&a22)&a33)
print((a11.intersection(a22)).intersection(a33))