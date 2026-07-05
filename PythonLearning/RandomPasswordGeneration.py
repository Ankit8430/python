import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

val=string.ascii_letters + string.digits + string.punctuation
# print(random.choice(val))

num=int(input("Enter the length of the password: "))
password=""
for i in range(num):
    password+=random.choice(val)

print("Your password is: ",password)