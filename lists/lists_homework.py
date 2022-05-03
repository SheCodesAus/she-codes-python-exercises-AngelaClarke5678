# Question 1
foods = ["orange","apple","banana","strawberry","grape","blueberry",["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]
#Question 1.1 The first item in the list.
print(foods[0])
#Question 1.2 The third item in the list.
print(foods[2])
#Question 1.3 The last item in the list.
print(foods[-1])
#Questions 1.4 The first three items in the list.
print(foods[0:3])
#Questions 1.5 The last three items in the list. List slicing https://www.geeksforgeeks.org/python-get-last-n-elements-from-given-list/
n = 3
last_3 = foods[-n:]
print("The last 3 elements of list are : " + str(last_3))
#Questions 1.6 The last item in the sublist.
print(len(foods))
print(foods[6])
print(foods[6][-1])

#Question 2 Format and print the following list:
mailing_list = [["Chilli", "chilli@thechihuahua.com"],["Roary", "roary@moth.catchers"],["Remus", "remus@kapers.dog"],["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],["Ivy", "noreply@goldendreamers.xyz"],]
print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")
print(f"{mailing_list[4][0]}: {mailing_list[4][1]}")

# Q3)Ask the user for three names, add them to a list,then print the list.
# completed_list = []
# maxLengthList = 6
# while len(completed_list) < maxLengthList:
#     input_name = input("Enter a name: ")
#     completed_list = completed_list.append(input_name)
#     print(completed_list)
# print(completed_list)

# Q3 attempt 2
# name1 = input("Enter a name: ")
# name2 = input("Enter a name: ")
# name3 = input("Enter a name: ")

# new_list = [name1, name2, name3]
# print(new_list)

#Q4 Using the following starter code, Produce the following lists
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

new_list2 = [[a] + [b] + [c]]
print(new_list2)

new_list3 = a + b + c
print(new_list3)