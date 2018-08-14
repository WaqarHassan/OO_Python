import os 
import random
import sys
import pdb 


class Animal(object):
  __name = ""
  __height = 0
  __weight = 0
  __sound  = 0

  def __init__(self,name,height,weight,sound):
    self.__name = name
    self.__height = height
    self.__sound = sound
    self.__weight = weight

  def set_name(self , name):
    self.__name = name

  def get_name (self):
    return self.__name

  def set_sound(self , sound):
    self.__sound = sound

  def get_height (self):
    return self.__height

  def set_height(self , height):
    self.__height = height

  def get_sound (self):
    return self.__sound

  
  def set_weight(self , weight):
    self.__weight = weight

  def get_weight (self):
    return self.__weight

  def get_type(self):
    print("Animal")

  def toString(self):
    return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
                                                                  self.__height,
                                                                  self.__weight,
                                                                  self.__sound)


class Dog(Animal):
  __owner = ""

  def __init__(self , name ,height, weight , sound , owner):
    self.__owner = owner
    super(Dog, self).__init__(name, height , weight, sound)

  def set_owner(self, owner):
    self.__owner = owner

  def get_owner(self):
    self.__owner

  def get_type(self):
    print("DOG")

  def toString(self):
    return "{} is {} cm tall and {} kilograms and say {} His owner is {}".format(self.get_name(),
                                                                  self.get_height(),
                                                                  self.get_weight(),
                                                                  self.get_sound(),
                                                                  self.get_owner())
  def multiple_sounds(self , how_many=None):
    if how_many is None:
      print(self.get_sound())
    else:
      print(self.get_sound() * how_many)


cat = Animal("whiskers" , 33 , 10 ,"Meow")
print(cat.toString())

spot = Dog("Spot",  53 , 27, "Ruff" , "Derek")

# pdb.set_trace()
print(spot.toString())


class AnimalTesting:
  def get_type(self , animal):
    animal.get_type()

test_animals  = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)
spot.multiple_sounds(4)
spot.multiple_sounds()