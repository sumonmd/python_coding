
n = int(input("Enter the element number:"))
ar = []
for i in range(0,n):
    ar.append(int(input("enter the element:")))

avg = sum(ar)/n
print("Average number is :", round(avg, 2))