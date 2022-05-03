#for loop
# for digit in range (1,6): #will print 1, 2, 3 4, 5, 6
#     print(digit)

# for digit in range (6): #will print 0, 1, 2, 3 4, 5,
#     #digit = 0
#     print(digit)

# numbers = [10,20,30,40]
# for number in numbers:
#     print(number)

# for num in range(10): #prints up to 9
#     print(num)

# for num in range(1,11): #prints up to 10
#     print(num)

# for num in range(0,11,2): #starts from 0, prints up to 11, every 2nd number
#     print(num)

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
# for item in range(len(chilli_wishlist)): #returns a range of 4 which is the lenght of the list
#     print(item)
#     print(chilli_wishlist[item]) #will prin the 4th item in the list
# for item in chilli_wishlist: #will print the list of items
#     print(item) 

chilli_wishlist = [
    ["igloo"],
    ["donut toy", "tennis ball", "crocodile toy"],
    ["chicken", "peanut butter"],
    ["cardboard box", "kong", "dig mat"]
]

for category in chilli_wishlist:
    # category 1 ["igloo"] LEVELS OF EXTRACTION
    #category 2 =    ["donut toy", "tennis ball", "crocodile toy"],
    for item in category:
        print(item)

#While loop, sytnax is a bit different to for loop it looks at a statement if true or not, if true it keeps running

# while 5 > 3:
#     print("hi") #will keep running we need a stopping statement

number = 1
while number > 0:
    print("hi") #need to change the number 
    number = 0 

guess = ""
while guess != "a":
    guess = input("guess a letter: ") #statement will keep running until guess = a
    print(guess)

counter = 10
while counter <= 10:
    print(counter)
    counter = counter +1 #will stop the statement because the 1 is now added
