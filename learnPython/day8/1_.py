from abc import ABC, abstractmethod
#
# class First():
#     def show(self):
#         print("this is from first")
#
#
# class Second(ABC):
#     @abstractmethod
#     def show(self):
#         pass
#
#
# class Third(Second, First):
#     pass
#
#
# t1 = Third()
# t1.show()

# when one of the parent is abstract class and other is normal
#   at time of inheritance it follows rule of leftmost first
#   if left class is abstract we need to implement abstract method
#   otherwise no need as normal class has implementation



# class First(ABC):
#     def show(self):
#        pass
#
#
# class Second(ABC):
#     @abstractmethod
#     def show1(self):
#         pass
#
#
# class Third(Second, First):
#     def show(self):
#         print("this is from third")
#
#
# t1 = Third()
# t1.show()

# from both abstract classes
# #############################################################################################################################

class First(ABC):
    @abstractmethod
    def show(self):
        pass


class Second(ABC):
    @abstractmethod
    def show(self):
        pass


class Third(Second, First):
    def show(self):
         print("this is of third")


t1 = Third()
t1.show()

#   it takes single implementation for both methods(show() of first and show() of second)
#   and therefore giving no error
#   this happens in all languages
#       when we inherited two abstract classes with same method

