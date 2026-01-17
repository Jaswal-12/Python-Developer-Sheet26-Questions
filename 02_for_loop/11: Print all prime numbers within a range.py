  x = int(input("Enter a number: "))

print("Prime numbers are:")

for i in range(2, x + 1):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)
