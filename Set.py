collection={1,2,3,4,"ankit",2}
print(collection)#{1,2,3,4,"ankit"}
print(type(collection))
print(len(collection))#5
collection1=set()
print(type(collection1))
collection1.add(1)
collection1.add(5)
collection1.add(2)
collection1.add(1)
print(collection1)
collection1.remove(2)
print(collection1)
collection1.clear()
print(collection1)

collection1.add("Aman")
collection1.add("Naman")
collection1.add("Ankit")
collection1.add("Vivek")
print(collection1)
collection1.pop()
print(collection1)

set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))