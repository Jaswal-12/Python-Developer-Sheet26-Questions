l = [9, 2, 3, 1, 5, 1, 6]


even=0
odd=0
for i in range(len(l)):
    if(l[i]%2==0):
        even=even+1
    elif(l[i]%2!=0):
        odd=odd+1

print(even)
print(odd)
