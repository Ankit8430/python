def fabonacci(n):
    a=0
    b=1
    if n<=0:
        print("Please enter a positive integer")
    elif n==1 or n==0:
        print()
    else:
        print(a, b, end=" ")
        for _ in range(2, n):
            c=a+b
            print(c, end=" ")
            a=b
            b=c

if __name__=="__main__":
    num=int(input("Enter the number: "))
    fabonacci(num)
    
