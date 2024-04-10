#!/usr/bin/python3
"""
class Square definition
"""

class Square():
   """
   Computes square properties
   """
   width = 0
   height = 0

   def __init__(self, *args, **kwargs):
       """
       initialization
       """
       for key, value in kwargs.items():
           setattr(self, key, value)
   
   def area_of_my_square(self):
       """ Area of the square """
       return self.width * self.height

   def permiter_of_my_square(self):
       """returns perimeter of square"""
       return (self.width * 2) + (self.height * 2)

   def __str__(self):
       """returns string represenation of an instance"""
       return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
