class Vector2:
    def __init__(self,x=0,y=0):
        self.x= x
        self.y =y
    def get(self):
        return (self.x,self.y)
    def set(self,_tuple):
        self.x,self.y=_tuple
        return self

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)
    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)
    def __floordiv__(self, other):
        return Vector2(self.x // other, self.y // other)
    def __eq__(self, other):
        return self.x==other.x and self.y == other.y
    def __ne__(self, other):
        return not (self.x==other.x and self.y == other.y)