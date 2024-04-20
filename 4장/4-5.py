def binary_search(A, key, low, high) :
    if (low <= high) :
        mid = (low + high) // 2
        if key == A[mid] :
            return mid
        elif key < A[mid] :
            return binary_search(A, key, low, mid-1)
        else :
            return binary_search(A, key, mid+1, high)
    return -1

listA = [1, 4, 7, 12, 15, 15, 25, 28, 30, 33, 40, 47, 50, 77]
print("입력 리스트 =", listA)
print("50 탐색(순환) -->", binary_search(listA, 50, 0, len(listA)-1) )
print("2 탐색(순환) -->", binary_search(listA, 2, 0, len(listA)-1) )
