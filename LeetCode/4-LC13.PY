s="III"

rome={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
val=0
for i in range(len(s)):
    temp=rome.get(s[i])
    temp2=0
    if (i+1 < len(s)) :
        t2=rome.get(s[i+1])
        if t2>temp:
            val=val-temp
    else:
        val=val+temp
print(val)
 
