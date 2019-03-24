dict = {}
a = 0
b = 1
for i in range(0,20):
    dict[i] = a
    x = b
    b += a
    a = x
n = int(input("Enter the number: "))
print(n,"th fibonacci number is :",dict[n-1])