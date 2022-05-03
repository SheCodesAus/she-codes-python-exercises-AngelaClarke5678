weather = "rainy"
name = "Angela"

# line 5 string variable
# print("Rainy")
# print(weather)

# Data Types 
# String is a text data
# integer  numerical data (whole number)
# Float numerical (with decimals)

height = 173
weight = 55.8
# print(type(name))
# print(type(height))
# print(type(weight))

day = "Saturday"
#print(type(day))
# print(type(day))
message = f"today is {day}!"
# print(message)

#Integers 
#run distance in m
run1_dist = 1400
run2_dist = 1800

#addition
total_dist = run1_dist + run2_dist
# print(total_dist)

#floats
#run distance in km
run3_dist = 1.7
run4_dist = 1.35

#addition2
total_dist = (run3_dist + run4_dist)
# print(total_dist)

#division and multiplication
print(run1_dist / 1000)
print(run4_dist * 1000)

#division always product floats
#other caclulations depend on the data type
# as long as there is one float, float
# float division & integer division

# different scenarios

name = "Angela"
run2_dist = 1800

# print(name + run2_dist)
# creates = TypeError: can only concatenate str (not "int") to str
# print(name * run2_dist)
# you can multipke a string and an integer

#typecast to change the data type
print(name + str(run1_dist))

print(name * int(run4_dist))
