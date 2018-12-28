# calculate factorial using recursive function

num = 10

def factorial(n):
    product = 1
    for x in range(1, num + 1):
        product *= x
    return product

print("{}! is {}".format(num, factorial(num)))


"""Now try using a recursive function"""

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)

print("{}! is {}".format(num, recursive_factorial(num)))