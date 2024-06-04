def knapSack_dc(W, wt, val, n):
    if n == 0 or W == 0 :
        return 0 # 종료 조건 
    
    if (wt[n-1] > W):
        return knapSack_dc(W, wt, val, n-1)
    else:
        valWithout = knapSack_dc(W, wt, val, n-1)
        valwith= val[n-1] + knapSack_dc(W-wt[n-1], wt ,val, n-1)
        return max(valwith, valWithout)

import random
import time

random.seed(0)  

val = [random.randint(1, 100) for _ in range(50)] # 물건들의 가치 리스트 
wt = [random.randint(1, 10) for _ in range(50)] # 물건들의 무게 리스트
W = 25 # 현재 배낭의 용량 
n = len(val)

start = time.time()
result = knapSack_dc(W, wt, val, n)
end = time.time()

print("0-1 배낭문제(분할정복):", result)
print("실행 시간: %.5f 초" % (end - start))

