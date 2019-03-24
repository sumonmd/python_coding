n = int(input("Enter the number: "))
check = 0
for i in range(2,n//2):
    if n%i==0:
        check = check + 1
if(check==0):
    print("This number is Prime")
else:
    print("This number is not prime")
