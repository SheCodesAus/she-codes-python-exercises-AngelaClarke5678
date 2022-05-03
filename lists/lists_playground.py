#Lists a list is more than 1 data and stored in square brackets
#we have 3 elements in the below list.
#python lists base on 0 index eg 0,1,2
numbers = [1,2,3]
characters = ["a", "b", "c"] 
print(characters)
print(type(characters))
print(characters[0])
#runs a
#we can add into our lists
characters.append("d")
#we can add multiple items to our list
characters.extend(['e','f'])
#we can insert items into list after a list item
characters.insert(1,"g")
print(characters)
#find the last element
print(characters[-1])
#find the list items, below brings up a, g
print(characters[0:2])

#delete elements, if we don't give index we get the last element
print(characters.pop(3))
print(characters)
print(characters.remove("a"))

