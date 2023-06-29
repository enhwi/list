list=[1,1,0,1]
i=-1
l=0-len(list)
a=0
c=0
while i>=l:
    if list[i]==1:
        a=list[i]
        c=2**1
        b=a*c
        c=c+b
    else:
        pass
    i=i-1
    c=c+1
print(c)