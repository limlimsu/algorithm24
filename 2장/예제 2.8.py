def factorial(n):
    result = 1
    for k in range(n, 0, -1):
        result = result * k 
    return result

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))