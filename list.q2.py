number=[50,40,23,70,56,12,5,10,7]
max=number[0]
i=0
while i<len(number):
    if max<number[i]:
        max=number[i]
    i=i+1
print(max)