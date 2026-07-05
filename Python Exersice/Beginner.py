# Square Cube
n=int(input("Enter a number"))
print(n**3)

# Swap two numbers (with and without a third variable).
a=10
b=20
a,b=b,a
print(a)
print(b)

# Check whether a number is even or odd.
n=int(input("Enter a number: "))
if n%2==0:
    print("Even number")
else:
    print("Odd Number")

# Check whether a number is positive, negative, or zero.
n=int(input("Enter a number: "))
if n<0:
    print("Negative Number")
elif n>0:
    print("Positive Number")
else:
    print("Zero Number")

# Find the largest of two numbers.
n1=int(input("Enter the first number: "))
n2=int(input("Enter second number: "))
if n1>n2:
    print(n1," is greater number")
else:
    print(n2," is greater number")

# Check whether a year is a leap year.
year=int(input("Enter a year: "))
if year%4==0:
    print("Leap Year")
elif year%100==0 and year%400==0:
    print("Leap Year")
else:
    print("Not Leap Year")

# Print the multiplication table of a number.
n=int(input("Enter a number: "))
for i in range(1,11):
    print(n," * ",i," = ",n*i)

# Find the sum of the first N natural numbers.
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

# Find the sum of even numbers from 1 to N.
n=int(input("Enter a number: "))
sum=0
for i in range(2,n+1,2):
    sum+=i

print(sum)

# Reverse a number.
n=input("Enter a number")
print(n[::-1])

# Count the digits in a number.
n=input("Enter a number: ")
print(len(n))

# Find the sum of digits of a number.
n=input("Enter a number: ")
sum=0
for i in range(len(n)):
    sum+=int(n[i])
print(sum)

# Check whether a number is a palindrome.
text=input("Enter a number: ")
if text==text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Check whether a number is an Armstrong number.
n=input("Enter a number: ")
sum=0
for i in range(len(n)):
    sum+=int(n[i])**len(n)

if int(n)==sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")

# Check whether a number is prime.
n=int(input("Enter a number: "))
isPrime=True

for i in range(2,n):
    if n%i==0:
       isPrime=False
if isPrime:
    print("Prime Number")
else:
    print("Not Prime Number")

