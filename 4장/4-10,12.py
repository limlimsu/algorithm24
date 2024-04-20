def kth_smallest_sort(A, k):
    A.sort()
    return A[k-1]

def partition(A, left, right) :
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high) :
        while low <= right and A[low] <= pivot : low += 1
        while high >= left and A[high]> pivot : high-= 1
        
        if low < high :
            A[low], A[high] = A[high], A[low]
            
    A[left], A[high] = A[high], A[left]
    return high

array = [11, 5 ,7, 8, 19, 17, 25, 20]
print("입력 리스트 =", array)
print("[정렬기법] 2번째 작은 수: ", kth_smallest_sort(array, 2))
print("[정렬기법] 4번째 작은 수: ", kth_smallest_sort(array, 4))

