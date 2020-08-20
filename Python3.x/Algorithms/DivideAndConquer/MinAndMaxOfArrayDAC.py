INF = float('inf')

def findMinAndMax(Array, i, j, min, max):
    if i == j :
        if min > Array[j]:
            min = Array[j]

        if max < Array[i]:
            max = Array[i]

        return min, max

    if j - i == 1:

        if Array[i] < Array[j]:
            if min > Array[i]:
                min = Array[i]

            if max < Array[j]:
                max = Array[j]

        else:

            if min > Array[j]:
                min = Array[j]

            if max < Array[i]:
                max = Array[i]

            return min, max
    mid = (i + j) // 2

    min, max = findMinAndMax(Array, i, mid, min, max)

    min, max = findMinAndMax(Array, mid+1, j, min, max)

    return min, max

if __name__ == '__main__':
    Array = [ 8,9,23,51,23,5,1,53,42,34,212,563]

    (min, max) = (INF, -INF)
    (min, max) = findMinAndMax(Array, 0, len(Array)-1, min, max )

    print("The minimum is : ", min)
    print("The maximum is : ", max)