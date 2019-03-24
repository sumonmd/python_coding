n = int(input("Enter the number "))
for i in range(1, n + 1):
    li = []
    for j in range(1, i+1):

        if j < i:
            print(j, "+", end=" ")
        else:
            print(j, end=" ")
        li.append(j)
    print("=", sum(li))

