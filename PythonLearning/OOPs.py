# class Student:
#     college="ABC College"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

# s1=Student("Ankit Gupta",85)
# print(s1.name)
# print(s1.marks)
# print(s1.college)
# s2=Student("Rohit Sharma",90)
# print(s2.name)
# print(s2.marks)
# print(s2.college)

# class Student:
#     college="ABC College"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def welcome(self):
#         print("Welcome ",self.name," to ",self.college)
    
#     def getMarks(self):
#         return self.marks

# S1=Student("Ankit Gupta",85)
# S1.welcome()
# print("Marks: ",S1.getMarks())


# class Student:
#     college="ABC College"
#     def __init__(self,name,math_marks,science_marks,english_marks):
#         self.name=name
#         self.math_marks=math_marks
#         self.science_marks=science_marks
#         self.english_marks=english_marks

#     def getAverage(self):
#         average=(self.math_marks+self.science_marks+self.english_marks)/3
#         return average
#     @staticmethod
#     def hello():
#         print("Hello Students")
    
# s1=Student("Ankit Gupta",85,90,80)
# print(Student.college)
# print("Average Marks of ",s1.name," is: ",s1.getAverage())
# Student.hello()

# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brake=False
#         self.clutch=False
    
#     def start(self):
#         self.acc=True
#         self.clutch=True
#         print("Car Started")
    
#     def stop(self):
#         self.acc=False
#         self.clutch=False
#         self.brake=True
#         print("Car Stopped")

# car1=Car()
# car1.start()
# car1.stop()

# class Account:
#     def __init__(self,balance,accountNo):
#         self.balance=balance
#         self.accountNo=accountNo

#     def debit(self,val):
#         self.balance=self.balance-val
    
#     def credit(self,val):
#         self.balance=self.balance+val
    
#     def printAccountInfo(self):
#         print("Account Number is: ",self.accountNo," and balance is: ",self.balance)

# acc1=Account(20000,1234)
# acc1.printAccountInfo()
# acc1.debit(10000)
# acc1.printAccountInfo()
# acc1.credit(20000)
# acc1.printAccountInfo()

# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("Ankit Gupta")
# print(s1)
# print(s1.name)
# del s1
# print(s1)
# print(s1.name)
# class Account:
#     def __init__(self,acc_num,acc_pass):
#         self.acc_num=acc_num
#         self.__acc_pass=acc_pass
#     def print_pass(self):
#         print(self.__acc_pass)
        
# acc=Account(123,456)
# print(acc.acc_num)
# acc.print_pass()

# class Person:
#     __name="Ankit"

#     def __hello(self):
#         print("Hello Person")

#     def welcome(self):
#         print(self.__hello(),self.__name)

# p1=Person()
# p1.welcome()


# class Car:
#     @staticmethod
#     def start():
#         print("Car Started")
    
#     @staticmethod
#     def stop():
#         print("Car Stopped")
    
# class Toyota(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(Toyota):
#     def __init__(self,type,brand):
#         self.type=type
#         super().__init__(brand)


# car1=Fortuner("Diesel","Toyota")
# car1.start()
# car1.stop()
# print(car1.brand)

# class Person:
#     name="Ankit Gupta"

#     def change_name(self,name):
#         self.name=name

# p1=Person()
# p1.change_name("Rohit Sharma")
# print(p1.name)
# print(Person.name)

# class Person:
#     name="Aman"

#     @classmethod
#     def change_name(cls,name):
#         cls.name=name

# p1=Person()
# p1.change_name("Rohit Sharma")
# print(p1.name)
# print(Person.name)

# a,b=1,3
# print(a+b)
# print(a.__add__(b))

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
    
#     def show_number(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)

# com=Complex(2,3)
# com.show_number()
# com2=Complex(4,5)
# com2.show_number()
# print("==========")
# com3=com + com2
# com3.show_number()

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius*self.radius
    
#     def perimeter(self):
#         return 2*3.14*self.radius
    
# circle1=Circle(5)
# print("Area of Circle is: ",circle1.area())
# print("Perimeter of Circle is: ",circle1.perimeter())

# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def show_info(self):
#         print("Role: ",self.role)
#         print("Department: ",self.dept)
#         print("Salary: ",self.salary)

# class Enginer(Employee):
#     def __init__(self,role,dept,salary,name,age):
#         super().__init__(role,dept,salary)
#         self.name=name
#         self.age=age
    
#     def show_info(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
#         super().show_info()

# e1=Enginer("Software Developer","IT",50000,"Ankit Gupta",25)
# e1.show_info()
    

# class Order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
    
#     def __gt__(self,order2):
#         if(order2.price>self.price):
#             print("Order 2 is greater than Order 1")
#         else:
#             print("Order 1 is greater than Order 2")

# o1=Order("Laptop",50000)
# o2=Order("Mobile",100000)
# o1>o2
