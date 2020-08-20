def binary_seach(arr, left, right, num):

    if right >= left:
        mid = (right + left) // 2

        if arr[mid] == num :
            return mid

        elif arr[mid] > num :
            binary_seach(arr, 0, mid, num)

        else:
            binary_seach(arr, mid+1, right, num)
    else :
        return -1

if __name__ == "__main__" :
    Array = [1,3,5,7,9,11,13,24,454,5745,34525,23453]

    k = binary_seach(Array, 0, len(Array)-1, 11)
    if k == -1:
        print("Not found")
    else:
        print("Number found at position : ", k+1)
