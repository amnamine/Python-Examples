def factorial(n,i):
    i=i-1
    if i == 0:
        return n
    else:
        return n * factorial(i,i)

num = int(input("Enter a number: "))
print("The factorial of", num, "is", factorial(num,num))
