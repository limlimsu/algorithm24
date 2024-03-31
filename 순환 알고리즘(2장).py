def factorial(n) :
    if n == 1 :
        return 1
    else :
        return n * factorial(n - 1)

print("1!: ", factorial(1)) 
print("3!: ", factorial(3))
print("5!: ", factorial(5))
