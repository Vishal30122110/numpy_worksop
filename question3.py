#write a program to find the factorial of a nummber
n=int(input())
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))
