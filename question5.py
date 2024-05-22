#write a program to find if the given number is prime no or not
n=int(input())
if n<=1:
    print("not prime")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break
else:
    print("not prime")
