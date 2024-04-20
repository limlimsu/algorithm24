def factorial_iter(n) :
    result = 1
    for k in range(1,n+1):
        result = result * k
    return result
    
n = 8
print(n, "factoriaal is ", factorial_iter(n))   


 