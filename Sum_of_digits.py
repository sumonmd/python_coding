n = int(input("Enter the number :"))
sum  = 0
while  n > 0:
    rem = n%10
    sum = sum + rem
    n = n//10
print(n,"Sum of the digit :",sum)
