

num = int(input("Enter the number :"))
n = num
pal = 0
while num > 0:
    rem = num % 10
    pal = pal*10 + rem
    num = num // 10
if n == pal:
    print("This number is palindrome ")
else:
    print("This number is not palindrome")