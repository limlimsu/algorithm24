def slow_power(x, n) :
    result = 1.0
    for i in range(n):
        result = result * x
    return result


import time
print("축소억지기법(2**500) =", slow_power(2.0, 500))

t2 = time.time()
for i in range(100000) : slow_power(2.0, 500)
t3 = time.time()

print("   억지기법 시간...", t3-t2)

