magic_square=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len (magic_square):
    j=0
    row=0
    while j<len(magic_square[i]):
        row=row+magic_square[i][j]
        j=j+1
    print(row)
    i=i+15
b=1
l=0
colom=0
while l<len(magic_square):
    while b<len(magic_square[l]):
     colom=colom+magic_square[b][l]
     
while a<len(magic_square):
  while b<len(magic_square):
    if a==b:
      dig=dig+magic_square[a][b]
      break
    b=b+1
  a=a+1
print(dig)
a=0
b=0
dig2=0
while len(magic_square)>a:
  while len (magic_square[a])>b:
      if a==b:
            dig2=dig2+magic_square[a][b]
            break
      b=b+1
  a=a+1
print(dig2)