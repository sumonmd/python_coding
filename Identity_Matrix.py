num = int(input("Enter the row column number by one integer number:"))

for i in range(0, num):
    for j in range(0, num):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
print()