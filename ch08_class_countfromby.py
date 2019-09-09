"""A simple class that has an increment function and magic methods y'all."""


class CountFromBy:
    # All the functions inside a class are called Methods
    def __init__(self, v: int = 0, i: int = 1):  # The first argument is always 'self'
        """__init__ is a 'magic-method' used to initialize class instances!"""
        # All the variables inside a class are called its attributes
        self.val = v
        self.incr = i

    def increase(self):
        """Increments 'val' by 'incr'."""
        self.val += self.incr
        print('Value incremented')

    def __repr__(self) -> str:
        """Another magic method that returns the canonical string representation of the object."""
        return "= {}, {} =".format(self.val, self.incr)  # Just want my data to look fancy


a = CountFromBy()
print('a is', a)
print(a.val, a.incr)
a.increase()
print(a)

b = CountFromBy(100)
print('\nb is', b)
print(b.val, b.incr)
b.increase()
print(b)

c = CountFromBy(22, 15)
print('\nc is', c)
print(c.val, c.incr)
c.increase()
print(c)
