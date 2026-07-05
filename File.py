"""
# Read
f=open("demo.txt","r")
data=f.readline()
print(data)
f.close()

#Overwrite all data
f=open("demo.txt","w")
f.write("I am learning python")
f.close()

#Append Data
f=open("demo.txt","a")
f.write(" with ML/AL")
f.close()

#Read
f=open("demo.txt","r")
data=f.read()
print(data)

f=open("demo.txt","r+")
f.write("abc")
f.close()

with open("demo.txt","r") as f:
    data=f.read()
    print(data)
"""

import os
os.remove("sample.txt")