import math
class Circle:
    def __init__(self, r = 1):
        self.r = r
    def setr(self,r):
        self.r = r
    def getr(self):
        return self.r

c = Circle()
c.setr(10)
print(c.getr())


