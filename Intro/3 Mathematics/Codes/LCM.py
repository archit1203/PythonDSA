def gcd(a,b):
        return a if b==0 else gcd(b,a%b)

a=int(input("A: "))
b=int(input("B: "))

print((a//(gcd(a,b)))*b)
