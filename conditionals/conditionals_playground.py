


# #comparison operators
# # == Equal
# # != not equal
# # > greater than
# # < less than
# # >= greater than or equal
# # <= Less than or equal

# # print(10 > 5) #as an answer you get a boolean type true
# # # we can compare floats and and integers
# # print (1 > 1.5)
# # print (5.9 != 5.8)

# # #compare strings
# # print("Asli" == "Jenny") #False
# # print("Asli" == "asli") #False, uppercase
# # print(3 == 3.0)
# # print(type(3) == type(3.0)) #False because one is Int and one is Float

# # temparature = 16
# # print(temparature < 18)
# # wind_chill = 3
# # print(wind_chill>4)
# # print(temparature - wind_chill < 16)
# name = "Camilla"
# # print("hayley" == name)

# #if statement
# if 5 > 4:
#     print("hello")

# if name == "Angela":
#     print("Hello again")
# elif name == "Camilla": #short for ELSE IF
#     print(f"Hello {name}, what are we doing today?")
# else:
#     print("wow hello I missed you")

is_raining = False
temperature = 16
wind_chill = 3
if temperature - wind_chill < 16 and is_raining:
    print("stay home")
else:
    if is_raining:
        print("you'll need an umbrella")
    elif temperature - wind_chill < 16:  
        print("you'll need a jumper today")


# if is_raining: 
#     print("take an umbrella")
# else: 
#     print("no umbrella needed")

# if temperature - wind_chill < 16:
#     print("take a jumper")
# elif temperature - wind_chill > 30:
#     print("stay home")
# else:
#     print("perfect day")

