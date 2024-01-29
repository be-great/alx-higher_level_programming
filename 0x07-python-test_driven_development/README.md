0x07. Python - Test-driven development
# General

    Why Python programming is awesome
    What’s an interactive test
    Why tests are important
    How to write Docstrings to create tests
    How to write documentation for each module and function
    What are the basic option flags to create tests
    How to find edge cases


## commands used:-

    $ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2    
    $ python3 -c 'print(__import__("<filename>").__doc__)' | wc -l
    $ python3 -c 'print(__import__("<filename>").<function_name>.__doc__)'

#### Cpython run:-
    $ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/local/include/python3.4m 102-python.c
