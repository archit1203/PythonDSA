t=(10,20,30,40,50)

#t2=(x for x in t)
#print(type(t2))

li=[]

for x in reversed(t):
    li.append(x)

li=tuple(li)
print(li,type(li)) 