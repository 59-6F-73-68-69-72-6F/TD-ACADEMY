# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2025-07-02
# email   = rudyleti@gmail.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""

import pprint as pp


class Object:
   def __init__(self, name):
      self.name = name
      self.tx = 0.0
      self.ty = 0.0
      self.tz = 0.0
      self.rx = 0.0
      self.ry = 0.0
      self.rz = 0.0
      self.sx = 1.0
      self.sy = 1.0
      self.sz = 1.0
      self.r = 255
      self.g = 255
      self.b = 255
      
   def translate(self, x: float, y: float, z: float) -> None:
      self.tx = x
      self.ty = y
      self.tz = z

   def rotate(self, x: float, y: float, z: float) -> None:
      self.rx = x
      self.ry = y
      self.rz = z

   def scale(self, x: float, y: float, z: float) -> None:
      self.sx = x
      self.sy = y
      self.sz = z
   
   def update_transform(self, ttype, *value) -> None:
      transform_methods = {
         "translate": self.translate,
         "rotate": self.rotate,
         "scale": self.scale
      } 
      if ttype in transform_methods:
         transform_methods[ttype](*value)
   
class Cube(Object):
   
   """
   By inheriting from a parent 'Object'class,the Cube reuses common transformation logic (translate, rotate,scale) without duplicating code.
   This makes it easy to create other types of objects (like a Sphere or Pyramid) that share the same basic transform properties.
   """
   
   def __init__(self, name):
      super().__init__(name)
      self.name = name
      
   def color(self, r: int, g: int, b: int) -> None:
      self.r = r
      self.g = g
      self.b = b
      
   def print_status(self):
      status = {
         "name": self.name,
         "translate": (self.tx, self.ty, self.tz),
         "rotate": (self.rx, self.ry, self.rz),
         "scale": (self.sx, self.sy, self.sz),
         "color": (self.r, self.g, self.b)
         }
      pp.pprint(status,sort_dicts=False)
 
 # Example usage     
cube1 = Cube("Cube1")
cube1.color(255, 0, 0)
cube1.update_transform("translate", 1.0, 2.0, 3.0)
cube1.update_transform("rotate", 45.0, 90.0, 180.0)
cube1.update_transform("scale", 2.0, 2.0, 2.0)
cube1.print_status()