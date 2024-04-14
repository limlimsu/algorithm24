def sequential_search(A, key):
    for i in range(len(A)) :
      if A[i] == key :
        return i
    
  
A = [1, 2, 3, 4, 5]
key = 2

result = sequential_search(A, key)

print("결과: ", result)