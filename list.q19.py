lists=[['g','f','g'],['i','s'],['b','e','s','t']]
i=0
list1=[]
while i<len (lists):
    j=0
    while j<len(lists[i]):
        list1.append(lists[i][j])
        j=j+1
    i=i+1
print(list1)
k=0
sum=''
while k<len(list1):
    sum=sum+list1[k]
    k=k+1
print(sum)