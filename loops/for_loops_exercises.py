# # Q1) Ask the user for a number. Use a for loop to print the times tables for that number
# number = int(input("Enter a number: "))
# print("The Multiplication Table of: ", number)  

# for count in range(1, 13):      
#    print (number, 'x', count, '=', number * count)

# #Q1Asli)
# number = int(input("Enter a number: "))

# for i in range(1,number+1):
#     print(i)
#     print(f"{number}*{i} = {number *1}")


#Q2) Ask the user for a number. Use a for loop to sum from 0 to that number.
n = int(input("Enter a number: "))
for count in range(0,n):
    print(f"{n}+{count}: {n+count}")
    n = n+count
print(n)

# Q3) Given a list, use a for loop to sum all the numbers in the list.
random_numbers = [3, 5, 9, 1] 
print(sum(random_numbers))

# Q4) Use a for loop to format and print the following list:
mailing_list = [
["Chilli", "chilli@thechihuahua.com"],
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Ivy", "noreply@goldendreamers.xyz"],
]
for items in mailing_list:
    print(items)