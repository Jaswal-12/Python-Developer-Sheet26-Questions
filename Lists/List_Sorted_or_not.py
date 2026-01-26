l = [1, 2, 3, 4, 5, 6]

x = 0
for i in range(len(l) - 1):
    if l[i] >= l[i + 1]:
        x = 1
        break

if x == 1:
    print("false")
else:
    print("true")
