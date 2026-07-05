""""""""" Calculate Sum of two numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
#Calculate Sum of two numbers
sum=num1 + num2
print(sum)
"""
"""Calculate area of size
side=int(input("Enter your side: "))
area=side*side
print("Area of ",side," is :", area)
"""
"""Calculae Average
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
average=(num1 + num2)/2
print(average)
"""
"""Find Greater Number
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print(num1) if num1>=num2 else print(num2)
"""
"""Take str from User and Print len
firstName=input("Enter the first name: ")
print(len(firstName))
"""
""" Find the occurence $ in a string
str="adfg$ergh1$sd"
print(str.count("$"))
"""
"""Even or Odd
num=int(input("Enter a number: "))
if(num%2==0):
    print("Even Number")
else:
    print("Odd Number")

"""
"""Find the Greatest of 3 number enter by users
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the thrid number: "))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
"""
"""Number is Multiple by 7 or not
num=int(input("Enter the number: "))
if num%7==0:
    print("Yes, Number is can multiple by 7")
else:
    print("No")

"""
"""3 Favo movie add to list
movie1=input("Enter first favorite movie: ")
movie2=input("Enter first favorite movie: ")
movie3=input("Enter first favorite movie: ")
movies=[]
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)
"""
"""Palidrom
list1=[1,2,5,4,2,1]
list2=list1.copy()
list2.reverse()
print(list1)
print(list2)
if list1==list2:
    print("Palindrom")
else:
    print("No")
"""
"""Count Number of student with A Grade
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))
"""
"""Store the above value in List and Store A to D
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)
"""
"""Store Dictonary 
dict={
    "table":["a piece of furniture","list of facs & figures"],
    "cat":"a small animal"
}
print(dict)
"""
"""How many classroom needs
set1={"Python","Java","C++","Python","JavaScript","Java","Python","Java","C++","C"}
print(set1)
print(len(set1))
"""
"""Enter subject from user
marks1=int(input("Enter the math marks: "))
marks2=int(input("Enter the phy marks: "))
marks3=int(input("Enter the chem marks: "))
dict={}
dict["Math"]=marks1
dict["Physics"]=marks2
dict["Chemistry"]=marks3
print(dict)
"""
"""Store same value but different data type
set1={
    ("int",9),
    ("float",9.0)
}
print(set1)
"""
"""Print Number from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
"""
"""Print number from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
"""
"""Print Table
num=int(input("Enter the number: "))
i=1
while i<=10:
    print(num," * ",i," = ",num*i)
    i+=1
"""
"""Print Square till Nth
n=int(input("Enter the number: "))
i=1
while i<=n:
    print(i*i)
    i+=1
"""
""""Search number in the tuple
tup=(1,4,9,16,25,36,49,64,81,100)
n=int(input("Enter the number: "))
i=1
while i<len(tup):
    if(tup[i]==n):
        print(i)
    i+=1
"""
"""Print Element using for loop
list=[1,4,9,16,25,36,49,64,81,100]
for element in list:
    print(element)
"""
"""Search Elem
tup=(1,4,9,16,25,36,49,64,81,100)
for ele in tup:
    if ele==34:
        print("Present")
        break
else:
    print("Not Present")
"""
"""Print from 1 to 100
for ele in range(1,101):
    print(ele)
"""
"""Print from 100 to 1
for ele in range(100,1,-1):
    print(ele)
"""
"""Table
n=5
for ele in range(5,51,5):
    print(ele)
"""
"""Sum of nth number
num=int(input("Enter the number: "))
i=1
sum=0
while i<=num:
    sum+=i
    i+=1
print(sum)
"""
"""Factorial
n=int(input("Enter the numbers: "))
fact=1
for ele in range(1,n+1):
    fact*=ele
print(fact)
"""
"""Print Length of List
def length(list):
    return len(list)
list=[1,3,4,5,6]
print(length(list))
"""
"""Print list element in the single line
def printList(list):
    for ele in list:
        print(ele,end=" ")

list=[1,2,3,4,5]
printList(list)
"""
"""Factorial Number
def fact(n):
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    return fact

num=int(input("Enter the number: "))
print(fact(num))
"""
"""Convert USD To INR
def convertUSTtoINR(currency):
    if currency=="USD":
        return "INR"
print(convertUSTtoINR("USD"))
print(convertUSTtoINR("INR"))
"""
"""Check number is odd or even
def checkNumber(num):
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")

checkNumber(5)
checkNumber(4)
"""
"""Recursion Factorial
def fact(n):
    if (n==0 or n==1):
        return 1
    return n*fact(n-1)

n=int(input("Enter the number: "))
print(fact(n))
"""
"""Sum of Nth Natural Number
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

print(sum(5))
"""
"""Print List using Recursion
def printList(i,n,list):
    if i==n:
        print(list[i])
        return
    else:
        print(list[i])
    printList(i+1,n,list)

list=[1,2,3,4,5]
printList(0,len(list)-1,list)
"""
"""Create a file
f=open("practice.txt","a")
f.write("Hi everyone \nwe are learning File I/O  using Java.\nI like programming in Java")
f.close()
"""
"""Replace Java to Python
with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

with open("practice.txt","r") as f:
    data=f.read()
    print(data)

with open("practice.txt","r") as f:
    data=f.read()
    if(data.find("learning")):
        print("Present")
    else:
        print("Not Present")
"""
"""Check for Line
def check_for_line():
    word="learning"
    data=True
    lineNo=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(lineNo)
                return
            lineNo+=1

check_for_line()
"""
"""Count even number
count=0
with open("practice.txt","r") as f:
    data=f.read()
    num=data.split(",")
    for val in num:
        if int(val)%2==0:
            count+=1
print(count)
"""
