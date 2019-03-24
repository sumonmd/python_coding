n = int(input("Enter the Year: "))

if n%400==0:
    print(n, end=" This year is a leap year")
elif n%4==0 and n%100!=0:
    print(n, end=" This year is Leap Year")
else:
    print(n, " This year is not leap year")