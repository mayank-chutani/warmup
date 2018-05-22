/*
 * Complete the sort function below.
 */

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
static SinglyLinkedListNode sort(int k, SinglyLinkedListNode list) {
    /*
     * Write your code here.
     */
    SinglyLinkedListNode end = list;
    for (int i=0; i<k-1 && end.next != null; i++)
        end = end.next;
    if (end.next==null)
        return mergeSort(list);

    SinglyLinkedListNode rest = sort(k, end.next);
    end.next = null;
    list = mergeSort(list);

    end = list;

    while (end.next != null)
    end = end.next;
    end.next = rest;

    return list;
}

static SinglyLinkedListNode sortedMerge(SinglyLinkedListNode a , SinglyLinkedListNode b) {
    SinglyLinkedListNode result = null;

    if (a == null)
        return b;
    if (b == null)
        return a;

    if (a.data <= b.data) {
        result = a;
        result.next = sortedMerge(a.next, b);
    }
    else {
        result = b;
        result.next = sortedMerge(a, b.next);
    }
    return result;
}

static SinglyLinkedListNode findMidPoint(SinglyLinkedListNode h) {
    if (h == null) {
        return h;
    }
    SinglyLinkedListNode fastPointer = h.next;
    SinglyLinkedListNode ptr = h;

    while (fastPointer != null) {
        fastPointer = fastPointer.next;
        if(fastPointer != null) {
            ptr = ptr.next;
            fastPointer = fastPointer.next;
        }
    }
    return ptr;
}

static SinglyLinkedListNode mergeSort(SinglyLinkedListNode h) {
    if (h == null || h.next == null) {
        return h;
    }

    SinglyLinkedListNode mid = findMidPoint(h);
    SinglyLinkedListNode midNext = mid.next;

    mid.next = null;
    SinglyLinkedListNode left = mergeSort(h);
    SinglyLinkedListNode right = mergeSort(midNext);

    SinglyLinkedListNode sortedList = sortedMerge(left, right);
    return sortedList;
}
