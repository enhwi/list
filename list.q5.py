num=int(input("enter number"))
i=2
while i<=num//2:
    if num%i==0:
        print("it is not prime")
        break
    else:
         print("it is  prime")
    i=i+1