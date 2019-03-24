def binary_search(list_item, item):
    ft = 0
    lt = len(list_item)-1
    mid = 0
    pos = 0
    while ft <= lt:
        mid = (ft + lt) // 2
        if list_item[mid] == item:
            return mid
        else:
            if item < list_item[mid]:
                lt = mid - 1
            else:
                ft = mid + 1
    return "no"

list = [1,3,4,5,6]
print(list)
pos = binary_search(list, 55)
if pos=="no":
    print("Not found")
else:
    print("position is :",pos+1)
