print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

print("Select operation (1/2/3/4): ")
choice=int(input())


match choice:
    case 1:
        print("Result: ",num1+num2)
    case 2:
        print("Result: ",num1-num2)
    case 3:
        print("Result: ",num1*num2)
    case 4:
        print("Result: ",num1/num2)
    case _:
        print("Invalid Input")
