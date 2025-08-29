#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        if value <= 0:
            raise ValueError("size must be positive")
        self._size = value

    def cobble(self):
        self.condition = "New"          # create the attribute
        print("Your shoe is as good as new!")  # print the exact message
