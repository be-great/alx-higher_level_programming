#!/usr/bin/python3
"""
class will be the “base” of
all other classes in this project
"""
import json


class Base:
    """
    this a the base class
    to manage the id attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """args: (int) id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string representation of list_objs to a file
        args:
            (List) of instances who inherits of Base list of Rectangle
            or list of Square instances
            Example:-
                r1 = Rectangle(10, 7, 2, 8)
                r2 = Rectangle(2, 4)
                Rectangle.save_to_file([r1, r2])

        """
        file = cls.__name__ + ".json"
        with open(file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                # get the dictorny of each on the list_objs
                save = [x.to_dictionary() for x in list_objs]
                f.write(json.dumps(save))

    @staticmethod
    def from_json_string(json_string):
        """args : (str) my_str"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary is None or dictionary == {}:
            return
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """"returns a list of instances"""
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, "r") as file:
                # load
                load = Base.from_json_string(file.read())
                for lo in load:
                    result.append(cls.create(**lo))
        except IOError:
            result = []
        return result
