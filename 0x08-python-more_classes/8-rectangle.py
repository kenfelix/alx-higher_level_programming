#!/usr/bin/python3
"""Area and Perimeter
"""


class Rectangle:
    """Defines the implementation of a rectangle
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieves the width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setd the height value"""
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """returns the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.height + self.width))

    def __str__(self):
        """Returns the rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """return a string representation of the rectangle"""

        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
