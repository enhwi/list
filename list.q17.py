b=[2,4,6,5,7,13,8,21,15,10,5]
i=0
even=0
odd=0
while i<len(b):
    if i%2==0:
        even=even+1
    elif i%2!=0:
        odd=odd+1
    i=i+1
print("even count=",even)
print("odd count=",odd)