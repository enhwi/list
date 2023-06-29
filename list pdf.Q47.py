str=["Red","Maroon","yellow","Olive"]
i=0
l=[]
while i<len(str):
    j=0
    c=[]
    while j<len (str[i]):
        c.append (str[i][j])
        j=j+1
    i=i+1
    l.append(c)
print(l)