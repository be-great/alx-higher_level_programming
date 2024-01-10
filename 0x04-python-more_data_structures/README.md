# 0x02. Python - import & modules
## General

1- Why Python programming is awesome

    Interprated language , oop , dynmaic type , cross_platform , general_purpose programming 

2- What are lists and how to use them
    
     are buildin data type of python which can contain collection of item.
Using : arr1 = []
3- What are the differences and similarities between strings and lists

    diff:
        A - string can't be modify 
            str = "hello"
            str[1] = "t"
        B- string is a sequence of character , list can contian different data type
        c - each have there own method and operation.
    similarities:
        A- indexing B- slicing "str[:n] + str[n+1:]" C- iteration

4- What are the most common methods of lists and how to use them

    A- append item at the end of list (stack) : list.append(6)
    B- pop item at specified position : list.pop(2)
    C- remove the first item on the list: list.remove()

5- How to use lists as stacks and queues

| Data structures | methods |
|---|---|
|stacks|push : list.append() , pop  : item =list.pop()|
|Queues|`from collections import deque`
         initialize: queue = deque()
         Enqueue   : queue.append(2)
         Dequeue   : queue.popleft()|


6- What are list comprehensions and how to use them

    A way of creating list : new_list = [expression for item in iterable if condition]


7- What are tuples and how to use them

    Another data type : A- that can be modified
                    B- faster and less memory cosuming
                    C- doesn't have buildin function in it

8- When to use tuples versus lists

    A- when you need const collection of element you don't want to modify 
    B- when you want faster and less consuming memory then the list


9- What is a sequence

    is collection of items. in python there is many sequence that share common characteris : indexing , slicing , iteration
    A- lists
    B- tuple
    C- strings
    D- list comprehensions
    E- ranges

10- What is tuple packing and sequence unpacking 

    A- tuple packing   : creating a tuple by grouping item saperated by comma :-  _tuple = 1, 2, 3

    B- sequence unpacking : is to assign the packing tuple into a variables
                        b, c, d = _tuple

12- What is the del statement and how to use it

    is statement that delete reference to object
    A- list : del list[2]  # delete giving index
    B- tuple : del _tuple  # delete the entire typle
    C- string: del _string # delete the entire string

## Files
|File | description|
|---|---|
|0-print_list_integer.py| function that prints all integers of a list.|
|1-element_at.py| function that retrieves an element from a list like in C.|
|2-replace_in_list.py|function that replaces an element of a list at a specific position (like in C).|
|3-print_reversed_list_integer.py|function that prints all integers of a list, in reverse order.|
|4-new_in_list.py|function that replaces an element in a list at a specific position without modifying the original list (like in C).|
|5-no_c.py|function that removes all characters c and C from a string.|
|6-print_matrix_integer.py| function that prints a matrix of integers.|
|7-add_tuple.py| function that adds 2 tuples.|
|8-multiple_returns.py|  function that adds 2 tuples. |
|9-max_integer.py|  function that finds the biggest integer of a list.|
|10-divisible_by_2.py|  function that finds all multiples of 2 in a list.|
|11-delete_at.py|function that deletes the item at a specific position in a list.|
|12-switch.py|switch value of a and b|
|13-is_palindrome.c, lists.h| function in C that checks if a singly linked list is a palindrome.|
|100-print_python_list_info.c| function that prints some basic info about Python lists.|
