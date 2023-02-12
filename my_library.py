from math import factorial

def combinations (k, n):
    return factorial(n) // (factorial(k) * factorial(n-k))

def arrangements (k, n):
    return factorial(n) // factorial (n-k)

