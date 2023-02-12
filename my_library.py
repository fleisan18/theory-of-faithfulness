from math import factorial, e

def combinations (k, n):
    return factorial(n) // (factorial(k) * factorial(n-k))

def arrangements (k, n):
    return factorial(n) // factorial (n-k)

def Bernoulli (k, n, p):
    return combinations(k, n) * p**k * (1-p)**(n-k)

def Poisson_distribution (k, n, p):
    l = n * p
    return l**k * e**(-l) / factorial(l) 


