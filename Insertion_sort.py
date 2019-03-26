def show_list(arr):
    print("Sorted List :", end=" ")
    for j in range(0, len(arr)):
        print(arr[j], end=", ")


def insertion_sort(arr):
    length = len(arr)
    for i in range(0, length):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1
    show_list(arr)


n = int(input("Enter the number the element:"))
arr = []
for i in range(0, n):
    a = int(input())
    arr.append(a)

insertion_sort(arr)
