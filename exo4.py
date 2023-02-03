def factoriel(n):
    i=1
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact    
print(factoriel(5))