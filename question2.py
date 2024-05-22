# find if the given number is a palindrome or not?
n=int(input())
temp=n
rev=0
while(n!=0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if rev==temp:
    print("palindrome")
else:
    print("not")
