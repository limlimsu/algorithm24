def knapSack_dp(W, wt, val, n):
    A = [[ 0 for x in range (W + 1 )] for x in range ( n + 1 )]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else :
                valWith = val[i-1] + A[i-1][w-wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)

    return A[n][w]

import random
import time

random.seed(0)  
val = [random.randint(1, 100) for _ in range(50)] # 물건들의 가치 리스트 
wt = [random.randint(1, 10) for _ in range(50)] # 물건들의 무게 리스트
W = 25 # 현재 배낭의 용량 
n = len(val)

start = time.time()
result = knapSack_dp(W, wt, val, n)
end = time.time()

print("0-1 배낭문제(동적계획):", result)
print("실행 시간: %.5f 초" % (end - start))