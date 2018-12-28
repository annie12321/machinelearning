def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = 10

print("The %dth fibonacci number is %d" % (num, fibonacci(num)))