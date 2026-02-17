n=17
if n==1:
        print(False)
for i in range(2,(n//2+1)):
        if n%i==0:
                print(False)
                break
else:
        print(True)
