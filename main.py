# print("Prashant Adhikari")
# print("Hello World")
# print("*" * 10)
# price = 10
# price = 10.2
# name = 'Prashant'
# is_published = True
# name = input('What is your name?')
# color = input("What is your favourite Color?")
# print("Hi" + name + "Is" + color + "your favourite color?")
from tkinter.font import names

#operators in python
#22//8 = 3 FOR the integer division
#22%8=6
#2**3 = 8

#birth_year = input("Your Birth year")
#age = 2019 - int(birth_year)
#print(age)
#print(type(age))

# weight = input("Your weight in pounds")
# weight_in_kilo = int(weight)/2.2
# print(int(weight_in_kilo))

# my_name = "Prashant"
# print(my_name[0])
# print(my_name[0:4])
# first = "Prashant"
# last = "Adhikari"
# # my_name = first + ' [' + last + ''] is a coder
# msg = f'{first} {last} is a coder'
# print(msg)


#string length function
# name = "Prashant Adhikari"
# print(len(name))

# print('Alice''Bob')        String concatination
# print('Alice' * 5)         String replication



#control statements
# name = "Prassdfsdf"
# if name == "Prashant":
#     print("Hello Prashant")
# elif name =="Sushan":
#     print("Hello Sushan")
# else:
#     print("i dont know you exactly")
#
# print('kid' if age < 18 else 'adult')


#switch cases
# day = 4;
# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case default:
#         print("other days")


#loops in python
#while loops
# var = 0
# while var<5:
#     print("Hello World")
#     var = var+1


#for loops
# pets = ['dog', 'cat', 'animal']
# for pet in pets:
#     print(pet)

# for i in range(5):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)


#function in python
# def sayHello(fname,lname):
#     print(f'Hello {fname}{lname}')
#
# sayHello('Prashant',' Adhikari')

# def sumNumbers(num1, num2):
#     sum = num1 + num2
#     return sum
#
# result = sumNumbers(1,3)
# print(result)

# for i in range(3):
#     for j in range(2):
#         print(f'{i}{j}')


#slices in lists
pets = ['dog','cat','cow','buffalo','rat'] # this is a example of lists
pets = ('dog','cat','cow','buffalo','rat') # this is a example of tuple
#key difference between tuple and the list is that the touple cannot be changed but the list can be changed

# print(len(pets))
# print(pets[0:2])
# pets.append('bed')
# pets.insert('bed')         these are the methods for the lists but tuples only do have the count index functions
# del pets[2]
# pets.remove("rat")
# print(len(pets))



#dictionaries
# my_pet = {
#     'name' : 'cat',
#     'size' : 'fat',
#     'color':'black'
# }
# my_pet['age'] = 3
# print (my_pet)
# print (my_pet[size])



#exception handling in python
# def divideNumbers(dividend, divisor):
#     try:
#         result = dividend / divisor
#         print(result)
#     except ZeroDivisionError:
#         print("you cannot divide by 0")
#
# divideNumbers(10,5)


#class and object in python
# class Car:
#     # Constructor to initialize attributes
#     def __init__(self, brand, color):
#         self.brand = brand  # Attribute: brand
#         self.color = color  # Attribute: color
#
#     # Method: Display details of the car
#     def display_details(self):
#         print(f"Car Brand: {self.brand}, Color: {self.color}")
#
#     # Method: Simulate driving
#     def drive(self):
#         print(f"The {self.color} {self.brand} is now driving.")
#calling object of the class car
# Creating objects of the Car class
# car1 = Car("Toyota", "Red")
# car2 = Car("Honda", "Blue")
#
# # Accessing methods
# car1.display_details()  # Output: Car Brand: Toyota, Color: Red
# car1.drive()            # Output: The Red Toyota is now driving.
#
# car2.display_details()  # Output: Car Brand: Honda, Color: Blue
# car2.drive()            # Output: The Blue Honda is now driving.


#creating class of your own
# class Dog:
#     _attr1 = "mammal"
#     _attr2 = "dog"
#     def fun(self):
#         print("I'm a", self._attr1)
#         print("I'm a", self._attr2)
# roger = Dog()
# print(roger._attr1)
# roger.fun()

#class with the constructor and the initiated function
# class GFG:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
#
#     def show(self):
#         print("Hello my name is " + self.name+" and I" +
#               " work in "+self.company+".")
#
#
# obj = GFG("John", "GeeksForGeeks")
# obj.show()




#attribute --> this is public
#_attribute --> this is for the protected
#__attribute --> this is for the private accessifiers




#Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"{self.name} makes a sound.")
#
# class Dog(Animal):  # Dog inherits from Animal
#     def speak(self):  # Overriding speak method
#         print(f"{self.name} barks.")
#
# dog = Dog("Buddy")
# dog.speak()  # Output: Buddy barks.
#
#





#polymerphism
# class Bird:
#     def fly(self):
#         print("Birds can fly.")
#
# class Penguin(Bird):
#     def fly(self):  # Overriding the fly method
#         print("Penguins cannot fly.")
#
# def demonstrate_flying(bird):
#     bird.fly()
#
# sparrow = Bird()
# penguin = Penguin()
#
# demonstrate_flying(sparrow)  # Output: Birds can fly.
# demonstrate_flying(penguin)  # Output: Penguins cannot fly.






#abstract class
# from abc import ABC, abstractmethod
#
# class Shape(ABC):  # Abstract class
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
# rect = Rectangle(4, 5)
# print(f"Area: {rect.area()}")        # Output: Area: 20
# print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 18
