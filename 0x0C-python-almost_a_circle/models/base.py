#!/usr/bin/python3
"""
class will be the “base” of
all other classes in this project
"""
import json
import csv
import turtle


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

    @staticmethod
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
                f.write(json.dump(save))

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """def save_to_file_csv(cls, list_objs)"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                else:
                    header = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=header)
                for ob_data in list_objs:
                    writer.writerow(ob_data.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes objects from a CSV file and create it"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r') as file:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                else:
                    header = ["id", "size", "x", "y"]

                writer = csv.DictReader(file, fieldnames=header)
                obj_list = []
                for dict_ in writer:
                    # create what we found on the csv file
                    d = {}
                    for key, value in dict_.items():
                        d[key] = int(value)
                    obj_list.append(d)
                res = []
                for obj_data in obj_list:
                    res.append(cls.create(**obj_data))
                return res
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        # setup the turtle screen
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Draw Rectangles and Squares")

        # create a turtle object
        drawer = turtle.Turtle()

        def draw_rectangle(rect):
            drawer.penup()
            drawer.goto(rect.x, rect.y)
            drawer.pendown()
            drawer.forward(rect.width)
            drawer.left(90)
            drawer.forward(rect.height)
            drawer.left(90)
            drawer.forward(rect.width)
            drawer.left(90)
            drawer.forward(rect.height)
            drawer.left(90)

        def draw_square(square):
            drawer.penup()
            drawer.goto(square.x, square.y)
            drawer.pendown()
            for _ in range(4):
                drawer.forward(square.size)
                drawer.left(90)

        for rect in list_rectangles:
            draw_rectangle(rect)

        for square in list_squares:
            draw_square(square)
