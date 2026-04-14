def sum(x):
    sum=0
    for i in range(1,x+1):
        sum+=i
    return sum

n=int(input("Enter: "))
print("SUM is : ",sum(n))   