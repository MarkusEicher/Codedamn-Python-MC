def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print(factorial(5))

def factorial2(n):
    return n * factorial2(n - 1) if n else 1

print(factorial2(5))