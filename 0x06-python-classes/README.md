# 0x06. Python - Classes and Objects
## General

    Why Python programming is awesome
    What is OOP
    “first-class everything”
    What is a class
    What is an object and an instance
    What is the difference between a class and an object or instance
    What is an attribute
    What are and how to use public, protected and private attributes
    What is self
    What is a method
    What is the special __init__ method and how to use it
    What is Data Abstraction, Data Encapsulation, and Information Hiding
    What is a property
    What is the difference between an attribute and a property in Python
    What is the Pythonic way to write getters and setters in Python
    How to dynamically create arbitrary new attributes for existing instances of a class
    How to bind attributes to object and classes
    What is the __dict__ of a class and/or instance of a class and what does it contain
    How does Python find the attributes of an object or class
    How to use the getattr function

## Files
|File | description|
|---|---|
|0-square.py|a class that do nothing|
|1-square.py|class Square that defines a square by: (based on 0-square.py) , Private instance attribute: size,Instantiation with size (no type/value verification)|
|2-square.py| Private instance attribute: size, Instantiation with optional size: def __init__(self, size=0). size must be an integer, otherwise raise a TypeError exception with the message size must be an integer , if size is less than 0, raise a ValueError exception with the message size must be >= 0|
|3-square.py|add Public instance method: def area(self): that returns the current square area|
|4-square.py|property def size(self): to retrieve it , property setter def size(self, value): to set it|
|5-square.py|Public instance method: def my_print(self): that prints in stdout the square with the character #|
|6-square.py| add Private instance attribute: position with it's getter and setter the of (,) the tuple[0] number of space to print at the beginning of each line , tuple[1] number of line to print before printing the square|
|100-singly_linked_list.py|create two class for the linked list : Node and linked list operation (insert and print)|
|101-square.py|Printing a Square instance should have the same behavior as my_print() : __str__|
|102-square.py|Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area: __eq__, __nq__, ...|
|103-magic_class.py|Python class MagicClass that does exactly the same as the following Python bytecode|