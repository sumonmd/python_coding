arr = [99, 21, 19, 22, 28, 11, 14, 18]


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def divide(arr):
    n = len(arr)
    if n < 2:
        return
    left = []
    right = []
    mid = n // 2
    for i in range(mid):
        left.append(arr[i])
    for i in range(mid, n):
        right.append(arr[i])
    divide(left)
    divide(right)

    merge(left, right, arr)


divide(arr)
for i in arr:
    print (i,end=",")
