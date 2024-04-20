def binary_search_iter(A, key, low, high) :
    while (low <= high) :
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1 

listA = [1, 4, 7, 12, 15, 15, 25, 28, 30, 33, 40, 47, 50, 77]
print("입력 리스트 =", listA)
print("7 탐색(반복) -->", binary_search_iter(listA, 7, 0, len(listA)-1) )
print("3 탐색(반복) -->", binary_search_iter(listA, 3, 0, len(listA)-1) )