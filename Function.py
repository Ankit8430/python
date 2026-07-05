"""
#Funtion
def sum(a,b):
    return a+b

#Function Call
print(sum(5,6))

#Average 3 Numbers

def average3Numbers(num1,num2,num3):
    return (num1+num2+num3)/3

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
print(average3Numbers(num1,num2,num3))

"""
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)