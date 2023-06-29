list=[[1,4,5],[1,3,4],[2,6]]
i=0
k=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        k.append(list[i][j])
        p=sorted(k)
        j=j+1
    i=i+1
print(p)