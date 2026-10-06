students = ["jarieu", "kamanda", "Mohamed", "yabom", "yankadie", "yankie", "yamarie"]
print(students)

print(f"the name of my best friend is {students[0]}")
print(f"the name of my best friend is {students[1]}")
print(f"the name of my best friend is {students[2]}")
print(f"the name of my best friend is {students[3]}")
print(f"the name of my best friend is {students[4]}")
print(f"the name of my best friend is {students[5]}")
print(f"the name of my best friend is {students[6]}")

print(students.index("jarieu"))
print(students.index("yabom"))
print(students.index("yankadie"))

students.append("deliliah")
print(students)

students = ["kadiatu", "caroline", "Donald"]
students.insert(4, "Donald")
print(students)

fruits = ["apple", "Banana", "Mango", "pineapple"]
students.extend(fruits)
print(students)

fruits.remove("Mango")

students.pop()
students.pop()
thirditem = students.pop()
print(students)
print(thirditem)