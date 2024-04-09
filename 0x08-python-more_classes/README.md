#  0x08. Python - More Classes and Objects :-

### General

1- What is Data Abstraction, Data Encapsulation, and Information Hiding
        Abstraction: Focuses on simplifying complex systems by highlighting essential features and behaviors, often expressed through abstract classes or interfaces.

        Encapsulation: Involves bundling data and methods into a single unit (class), hiding internal details and providing controlled access through methods.

        Hidden Information (Information Hiding): Restricts direct access to certain details of an object, enhancing modularity and security by controlling visibility and exposure of internal implementation.
    
2- What is a property

    These decorators `property` allow you to use the private attribute as if it were a normal attribute while providing control over the access, modification, and deletion of the underlying data. This enables the implementation of encapsulation and information hiding principles in Python classes.

3- What is the difference between an attribute and a property in Python

    an attribute is a variable associated with an object, while a property is a special attribute that uses getter, setter, and deleter methods to provide controlled access to the underlying data. Properties are often used to implement encapsulation and to enforce certain behaviors when getting, setting, or deleting values.
    
4- What are the special __str__ and __repr__ methods and how to use them
    
    Usage:

    __str__ is more for end-users and readability.
    __repr__ is more for developers and debugging.

By providing custom implementations for these methods in your classes, you can control how instances of those classes are represented as strings in various contexts. If __str__ is not defined, Python will use __repr__ as a fallback. If neither is defined, the default string representation will be used, which may not be very informative

5- What is a class method, What is a static method
   Static methods in Python are methods that are bound to a class rather than an instance of the class. They are defined using the @staticmethod decorator. The key points and purposes of static methods include:

    No Access to Instance or Class:
        Unlike regular methods and class methods, static methods don't have access to the instance (self) or the class (cls) as parameters. They operate in the context of the class but don't interact with specific instances or class attributes.

    
6- How to dynamically create arbitrary new attributes for existing instances of a class ,How to bind attributes to object and classes

    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Creating an instance
    person = Person("Alice", 30)

    # Dynamically adding a new attribute
    person.city = "New York"

    # Accessing the new attribute
    print(person.city)  # Output: New York


7- What is and what does contain __dict__ of a class and of an instance of a class

__dict__ of a Class and an Instance:

    # __dict__ of a Class: It contains the namespace of the class, including class attributes.
    # __dict__ of an Instance: It contains the namespace of the instance, including instance attributes.


    class MyClass:
        class_variable = 42

    print(MyClass.__dict__)
    # output : {'__module__': '__main__', 'class_variable': 42, '__dict__': <attribute '__dict__' of 'MyClass' objects>, ...}


8- How does Python find the attributes of an object or class

    A- instance (object) Namespace - if not found go to (B)
    B- class Namespace - if not found go to (C)
    C- parent classes - if not found go to (D)
    D- attribute error



|File | description|
|---|---|
|0-rectangle.py|a class that do nothing|
|1-rectangle.py||
|2-rectangle.py||
|3-rectangle.py||
|4-rectangle.py||
|5-rectangle.py||
|6-rectangle.py||
|7-rectangle.py||
|8-rectangle.py||
|9-rectangle.py||
|101-nqueens.py||
