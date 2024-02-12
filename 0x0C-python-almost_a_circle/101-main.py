#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(100, 110, 0, 0), Rectangle(100, 110, 100, 1)]
    list_squares = [Square(100,0, 110), Square(15, 100, 110), Square(80, 100, 110)]

    Base.draw(list_rectangles, list_squares)