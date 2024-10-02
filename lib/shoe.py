#!/usr/bin/env python3

class Shoe:
    

    def __init__(self, brand = "Adidas", size = 9, condition = "Old"):
        self.brand = brand
        self.size = size
        self.condition = condition


    @property
    def brand(self):
        return self._brand
    
    @property
    def size(self):
        return self._size
    
    @property
    def condition(self):
        return self._condition
    
    @brand.setter
    def brand(self,value):
        self._brand = value
    
    @size.setter
    def size(self,value):
        if isinstance(value,int):
            self._size = value
        else:
            print("size must be an integer")

    @condition.setter
    def condition(self,value):
        self._condition = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    