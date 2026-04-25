n=int(input("Enter number: ")
fact=1
if n==0 or n==1:
    return 1
if n<0:
    return -1
while(n):
    fact*=n
    n-=1
print(fact)
