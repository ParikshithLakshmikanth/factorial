def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)
    
num = int(input("Enter a Number: "))

if num<0:
    print("neagtive numbers not allowed")
elif num == 0:
    print("factorial in 0 or 1")
else:
    print("Factorial of",num,"is",factorial(num))