#key-value pairs
#keys are unique
# needs to be imutable - can't change
#unordered before 3.6v

# students = {"Zohre": 123, "dani": 555 }
# students["Donna"] = 189
# print(students)
# del students["dani"]
# students["Dani"] = 999
# print(students)

# students = {"Zohre": 123, "dani": 555 }
# for student in students.items():    
#     print(student) #creates tupple

# students = {"Zohre": 123, "dani": 555 }
# for student_name, student_numbers in students.items():    
#     print(f"student name is: {student_name}") 
#     print(f"student no is: {student_numbers}") 

# for i in student_numbers.keys():
#     print(i)

groceries = {"Baby Spinach": 2.78,"Hot Chocolate": 3.70,"Crackers": 2.10,"Bacon": 9.00,"Carrots": 0.56,"Oranges": 3.08,}
# print(groceries)
print(groceries["Baby Spinach"])
groceries["Hot Chocolate"] = 2.70 #update a price
print(groceries)
del groceries["Crackers"] #remove an item
print(groceries)

for item, price in groceries.items(): #iterate over the dictionary
    print(f"{item}: ${price}")