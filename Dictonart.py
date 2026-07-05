dict={
    "name":"ankit",
    "cgpa":9.6,
    "marks":[97,96,95]
}
print(dict)
print(type(dict))
print("Name: ",dict["name"])
print("Cgpa: ",dict["cgpa"])
print("Marks: ",dict["marks"])
dict["cgpa"]=10
print(dict)
dict["rollNumber"]=123
print(dict)
#Nested Dictonary
student={
    "name":"aman",
    "score":{
        "chem":90,
        "phy":85,
        "math":95
    }
}
print(student["score"]["math"])#95
print(student.keys())#dict_keys(['name', 'score'])
print(student.values())#dict_values(['Ankit', {'chem': 90, 'phy': 85, 'math': 95}])
print(student.items())#dict_items([('name', 'Ankit'), ('score', {'chem': 90, 'phy': 85, 'math': 95})])
print(student.get("name"))#Ankit
student.update(dict)
print(student)#{'name': 'ankit', 'score': {'chem': 90, 'phy': 85, 'math': 95}, 'cgpa': 10, 'marks': [97, 96, 95], 'rollNumber': 123}
print(len(student.keys()))#5