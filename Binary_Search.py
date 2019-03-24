def binary_search(list_item, item):
    ft = 0
    lt = len(list_item)-1
    found = "no"
    while ft <= lt and found != "yes":
        mid = (ft + lt) // 2
        if list_item[mid] == item:
            found = "yes"
        else:
            if item < list_item[mid]:
                lt = mid - 1
            else:
                ft = mid + 1
    return found

list = [1,3,4,5,6]
print(list)
print(binary_search(list, 7))
