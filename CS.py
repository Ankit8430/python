""" Trafic Light
light=input("Light: ")
if(light=="Red"):
    print("Stop")
elif(light=="Yellow"):
    print("Look")
elif(light=="Green"):
    print("go")
else:
    print("Light is broken")
"""

""" Marks
marks=int(input("marks: "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")"""
"""Fee Calculation
A=int(input("Age: "))
G=input("Gender: ")
if((A==1 or A ==2) and G=="M"):
    print("Fee is 100")
elif((A==3 or A==4) and G=="F"):
    print("Fee is 200")
elif(A==5 and G=="M"):
    print("Fee is 300")
else:
    print("No Fee")
    """

"""Ternary Operator"""
age=int(input("Age: "))
print("Vote") if age>=18 else print("Not Vote")