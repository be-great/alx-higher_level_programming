#  0x0B. Python - Input/Output 

General

1- How to open a file

    file = open("filename", 'r')
2- How to write text in a file

    # 1- file mehtod
    file = open("filename", 'w')
    file.write("dfdsfsd")
    file.close()
    # 2- second choose
    #  File is automatically closed with `with`
    Open the file in write mode
    with open('output.txt', 'w') as file:
        for i in range(5):
            text_to_write = f'This is line {i+1}\n'
            file.write(text_to_write)

3- How to read the full content of a file
    
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
    file.close()


4- How to read a file line by line
    
    file = open('example.txt', 'r')
    for line in file:
        print(line.strip())  # strip() removes newline characters
    file.close()

5- How to move the cursor in a file
    
    file= open("dfs", 'r')
    file.seek(10) # move to the 10 byte
    content = file.read() # read the content
    print(content)
    file.close()

6- How to make sure a file is closed after using it
    
    # with is auto close the file
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
8- What is JSON
    
    Shortcut: JavaScript object Notation
    benefits: is a lightweight data interchange format.easy of humans 
    and machines to read

9- What is serialization, deserialization

    - process of converting data structure into easy stored and transmitted, the deserialization is the opposite of that
    

11- How to convert a Python data structure to a 
    JSON string.

        import json
        data = {"name": "John", "age": 30}
        json_string = json.dumps(data)
        print(json_string)

12- How to convert a JSON string to a Python data structure

        json_string = '{"name": "John", "age": 30}'
        data = json.loads(json_string)
# Files
|Files|Discription|
|---|---|
|0-read_file.py||
|1-write_file.py||
|2-append_write.py||
|3-to_json_string.py||
|4-from_json_string.py||
|5-save_to_json_file.py||
|6-load_from_json_file.py||
|7-add_item.py||
|8-class_to_json.py||
|9-student.py||
|10-student.py||
|11-student.py||
|12-pascal_triangle.py||
|100-append_after.py||
|101-stats.py||
