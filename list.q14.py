x=[[0],[1,3],[5,7],[9,11],[13,15,17]]
length=len(x)
i=0
min=x[0]
max=x[0]
while (i<length):
    if (len(x[i])<len(min)):
        min=x[i]
    if (len(x[i])>len(max)):
        max=x[i]
    i=i+1
print(len(min),min)
print(len(max),max)     