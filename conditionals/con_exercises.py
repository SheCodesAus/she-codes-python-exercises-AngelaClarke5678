# Exercise 1 and 2 
moths_in_house = True
mitch_is_home = False

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
elif mitch_is_home and not moths_in_house:
    print("Climb on mitch")
else:
    print("No threats detected")

# Question 3

light_color = "Red"
car_detected = True

if light_color == "Red" and car_detected:
    print("Flash")
else:
    print("Do nothing")

# Question 4
height = input("Enter height: ")
height_input = int(height)

if height_input >= 120:
    print("Hop on")
else:
    print("Sorry not today :(")

# Question 5
username = input("enter username: ")
password = input("enter password: ")

if username == "fleur" and password  == "password123":
    print("Correct")
else:
    print("Incorect")

# Question 6
email = input("Enter email: ")

if  "@" and "." in email:
    print("Valid Email Address")
else:
    print("Not valid")