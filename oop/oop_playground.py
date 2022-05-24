# #prints all the things you can appluy om the list object because of the data typ

# a method is applied to a specific class type only. 

#a car can be a class eg a car can have a few states such as colour, make and model. It can behave in a certain way eg acceraltel, brake,
# a class is a structure
#we can create our own class by giving it a structure and that makes an object by looking at the structure of the card that we defined.

class Dog():
    #states - breed, age, weight
    def __init__(self, name, breed, age, weight): #self means status, attribute
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight

    #behaviour - eat, talk, sleep
    def talk(self):
        print("Bark, Bark")

    def eat(self):
        self.weight += 0.5

jet = Dog("Jett", "Pug", 3, 10)
lyra = Dog("Lyra", "Neo Mastiff", 7, 45.0)
king = Dog("King", "Staffy", 10, 30.0)

print(jet.name, jet.weight)
jet.eat()
jet.eat()
jet.eat()
print(jet.weight)