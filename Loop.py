"""While Loop
i=0
while i<=5:
    print("Hello")
    i+=1

n=5
i=1
while i<=10:
    print(i)
    if i==n:
        break
    i+=1
i=1
while i<=10:
    if i==n:
        i+=1
        continue
    i+=1
    print(i)
"""
"""For Loop
list=[1,2,3,4,5]
for el in list:
    print(el)

tup=(1,2,3,4,5)
for el in tup:
    print(el)
else:
    print("End Loop")
set={"ankit","aman","naman"}
for el in set:
    print(el)

dict={
    "name":"Ankit Gupta",
     "age":20
}
for el in dict.keys():
    print(el)
for el in dict.values():
    print(el)

"""
"""Range()
for ele in range(5):
    print(ele)
for ele in range(1,5):
    print(ele)
for ele in range(1,5,2):
    print(ele)
"""
