s='paradox'
n=3

l1='abcdefghijklmnopqrstuvwxyz'
rev=l1[::-1]
d1=dict(zip(l1,rev))

pre=s[0:n-1]
suf=s[n-1:]
mirror=''

for i in range(0,len(suf)):
    mirror=mirror+d1[suf[i]]

print(pre+mirror)