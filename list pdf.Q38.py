list=['.com', '.edu', '.tv']
i=0 
l="https://www.w3resource.net contains an element" 
while i<len(list): 
    if (list[i]) in l:
         match="true" 
    else: 
        match="false" 
        i=i+1 
print(match)