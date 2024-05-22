#write a program to find the sum of digits of a given number'
n=int(input())
sum=0
temp=n
rev=0
while n!=0:
    dig=n%10
    sum=sum+dig
    n=n//10
print(sum)
