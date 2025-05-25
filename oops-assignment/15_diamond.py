class A:
    def show(self):
        print("A")
# inherit A in B and C classes
class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")        


class D(B, C):
    pass
          

d= D()  
print(D.__mro__) # Method Resolution Order  
print(d.show()) # B