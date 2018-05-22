def merge(arr, l, m , r):
    n1 = m - l + 1
    n2 = r - m

    l1 = [0] * n1
    l2 = [0] * n2

    for i in range(len(l1)):
        l1[i] = arr[l + i]

    for i in range(len(l2)):
        l2[i] = arr[m + i + 1]

    i = 0
    j = 0
    k = l
    while (i < n1 and j < n2):
        if (l1[i] <= l2[j]):
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = l2[j]
            j += 1
        k += 1

    while (i < n1):
        arr[k] = l1[i]
        k += 1
        i += 1

    while (j < n2):
        arr[k] = l2[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if (l < r):
        m = l + int((r-l) / 2)
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

if __name__ == '__main__':
    arr = [6,3,5,8,0,1,2]
    mergeSort(arr, 0, len(arr)-1)
    print(arr)
