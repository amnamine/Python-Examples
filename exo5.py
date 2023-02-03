# Python code to demonstrate naive method
# to compute factorial
def factoriel(n):
    fact = 1

    for i in range(1, n+1):
        fact = fact * i
    return fact

print(factoriel(-2))