def fib_iter(n):
    if (n<2): return n
    last = 0
    current = 1
    for i in range(2, n+1):
        tmp = current
        current += last
        last = tmp
    return current

print(fib_iter(10))  