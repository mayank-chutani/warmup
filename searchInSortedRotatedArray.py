Search (arr, start, end, elem):
    Mid = 1 + (len(arr) - 1)/2
    if(arr[mid] == elem):
        Return True
    if(arr[start] <= arr[mid]):
        if (elem >= arr[start] and elem <= arr[mid]):
            Return search(arr, start, mid-1, elem)
        Return search(arr, mid+1, end, elem)

    If (elem >= arr[mid] and elem <= arr[end]):
        Return search(arr, mid+1, end, elem)

    Return search(arr, start, mid-1, elem)

891234567
234567891
123456789
789123456
678912345
