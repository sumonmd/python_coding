
n = int(input("Enter the number of element: "))
list_item = []
for i in range(0,n):
    a=input()
    list_item.append(a)

for i in range(0,n):
    for j in range(0,n-1):
        if list_item[j]>list_item[j+1]:
            temp = list_item[j]
            list_item[j]=list_item[j+1]
            list_item[j+1] = temp

print(list_item)
