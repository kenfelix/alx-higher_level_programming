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

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method that returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the '#' character."""
        if self.size == 0:
            print("")
            return
        for i in range(0, self.__position[1]):
            [print("")]
        for i in range(0, self.size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.size)]
            print("")
