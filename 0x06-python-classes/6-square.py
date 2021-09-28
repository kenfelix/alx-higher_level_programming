#!/usr/bin/python3
"""Square Module"""


class Square:
    """Defines a squre with a private instance attribute called size"""

    def __init__(self, size=0, position=(0, 0)):
        """instantializes a privated instance of a sqare"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """instatiation with opional size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Gets the size"""
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """instatiation with opional position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Gets the position"""
        self.__position = value

        if not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method that returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character # and postion spaces"""
        if self.__size == 0:
            print("")
        else:
            row = self.__size
            col = self.__size
            space_no = self.__position[0]

            for i in range(row):
                for k in range(space_no):
                    print(" ", end="")
                for j in range(col):
                    print("#", end="")
                print("")
