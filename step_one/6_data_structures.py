# list 有序、可修改
fruite = ["apple", "banana", "cherry"]


print()
print(fruite[0])
print()
print(fruite[-1])
print()
print(fruite[0:2])

fruite.append("data")
print("append: ")
print(fruite[0:4])

fruite.remove("apple")
print("remove: ")
print(fruite)

print("len: ")
print(len(fruite))

for i in fruite:
     print(i)
     print()

fruite[1] = "a"
print("fruite[1]=", fruite[1])
# fruite[5] = "b"



# tuple  有序、不可修改
point = (3, 10)
print(point[0])
print(point[1])
# point[0] = 2
print()




# dict 
student = {"name": "xiaoming", "age": 10, "grade": "A"}
print(student["age"])
print()
print(student["name"])

student["name"] = "xiaohong"
print(student["name"])
print(student)
print()

student["score"] = 100
print(student["score"])

# student["happy"] = "yes"
print(student.get("sa", "false"))
print(student.pop("happy", "222"))
print()




# set — 无序、自动去重
numbers = {1, 2, 3, "4", 5}
print(numbers)

numbers.add(1)
numbers.add(1.3)
print(numbers)

numbers.discard(1)
print(numbers)

a = {1, 2, 3}
b= {3, 4, 5, 6}
print( "union: ", a | b)
print("intersection: ", a & b)
print("difference:(a有b没有)) ", a - b)
print("symmetric_difference:(只在一边出现的)", a ^ b)

print(3 in a | b)
print(10 in a | b)