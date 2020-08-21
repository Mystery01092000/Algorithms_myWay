def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # create two array left and right
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy the element of to array left and right i.e., L, R
    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]


    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


if __name__ == '__main__' :
    arr = [23, 54, 12, 63, 3, 21, 66, 44, 77, 22, 55, 6, 7, 98, 76, 54, 556]
    n = len(arr)
    mergeSort(arr, 0, n - 1)
    print("\n\nSorted array is")
    for i in range(n):
        print(arr[i], end=' '),