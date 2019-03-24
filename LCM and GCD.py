n1 = int(input("Enter the number1 :"))
n2 = int(input("Enter the number2 :"))
a = n1
b = n2

while b != 0:
    t = b
    b = a % b
    a = t
gcd = a
lcm = (n1*n2)/a
print(n1, " ", n2, "GCD is :", gcd)
print(n1, " ", n2, "LCM is :", lcm)