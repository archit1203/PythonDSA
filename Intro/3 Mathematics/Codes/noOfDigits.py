#WAP to write no of digits in number
num=(input("Enter a number: "))
count=0
if num.isdigit()==False:
    print("Not a number!")
    quit()
num=int(num)
while(num):
    count+=1
    num//=10
#print(f"No of digits= {count}")
print("No of 2digits= ",count)
