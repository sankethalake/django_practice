

# Diamond problem: which method is called when same method is present in both  parent classes
#   which are also inherited from a single class with show()

          #                         class A: show()
          # class B(A):show()                                   class C(A):show()
          #                         classD(B,B)




class A:
    def show(self):
        print("this is from A")


class B(A):
    def show(self):
        print("this is from B")


class C(A):
    def show(self):
        print("this is from C")


class D(B, C):
    pass

d1 = D()
d1.show()

# in scenario when both methods have same name
# method is called on basis of priority of inheritance of B and C in D
#   more precisely : left node of parent
# eg. we write: class D(B,C), show() from B is called

# show() method from  class A is not  called as it is overridden in class B


