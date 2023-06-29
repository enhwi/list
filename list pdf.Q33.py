list= [12, 67, 98, 34]
a=[]
for i in list:
    sum=0
    for j in str(i):
        sum=sum+int(j)
    a.append(sum)
print(a)