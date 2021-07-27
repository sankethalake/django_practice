# Abstraction: hiding internal implementation  details from user
#   not directly present in python:
#       need to use packages
# to use abstract class we need to inherit it
#    in inherited class we need to write implementation of abstractmethod

from abc import ABC, abstractmethod                 # these are the package used for abstract class


class AbstractClass(ABC):

    @abstractmethod                                  # if we not write this, we can create instance of this class(this is annotation)
    def abs(self):
        pass

    def show(self):
        print("this is method Body")

    def __init__(self):
        print("this is init method of abstract class")


# a1 = AbstractClass()      # can't instantiate class which has abstract method
# a1.show()


class InheritAbsClass(AbstractClass):
    def abs(self):
        print("abstract method implemented")


i1 = InheritAbsClass()
i1.show()
i1.abs()
