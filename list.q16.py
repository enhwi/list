elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
sum1=0
while i<len(elements):
    if elements [i]%2==0:
        sum=sum+elements[i]
    elif elements[i]%2!=0:
        sum=sum+elements[i]
    i=i+1
aveg_even=sum/i
aveg_odd=sum/i
print("aveg of even=",aveg_even)
print("aveg of odd=",aveg_odd)