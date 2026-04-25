n=555
num=n
num2=0
res=0
while(num):
    res=num%10
    #print(res)
    num2=num2*10+res
    num//=10
print(num,num2,n)
if num2==n:
    print(True)
else:
    print(False)
