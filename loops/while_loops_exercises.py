# # Q1) Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the numbers
# input_number = input("Enter a number: ")
# completed_list = []
# while input_number != "":
#     completed_list.append(int(input_number))
#     input_number = input("Enter a number: ")
#     print(input_number)
# print(completed_list)
# print(sum(completed_list))

# # alternate ways of doing it:
# sum=0
# userinput=0
# while userinput !="":
#         # userinput= (input("Enter Number : "))
#         sum=sum+(int(userinput)) 
#         userinput= (input("Enter Number : "))  
# else:
#     print (sum)
# Q2) Ask the user to enter a number. Print all the odd numbers between 0 and that number (inclusive).
user_number = int(input("Enter a number: "))
number = 1
while number <= user_number:
    if number %2 != 0:
        print(f"{number}")
    number = number +1

# Q3) Select a number. Ask the user to enter a number, output whether their number is less than or greater than the selected number. Repeat this process until the user guesses the correct number.
number = 7
guess_number = int(input("Guess the number: "))
while number != guess_number:
    if guess_number < number:
        print("Too low!")
        # guess_number = int(input("Guess the number: "))
    elif guess_number > number:
        print("Too High!")
    guess_number = int(input("Guess the number: "))
print("Correct!")
