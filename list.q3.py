list=[50,40,23,70,56,12,5,10,7]
max=list[0]
i=0
while i<len(list):
    if max<list[i-1]:
        max=list[i]
    i=i+1
print(max)