"""Geometric figures"""

class Figure:


    def __init__(self, colour):
        self.colour = colour


class Square(Figure):

    def __init__(self, colour, side_a, side_b):
        super().__init__(colour)
        self.side_a = side_a
        self.side_b = side_b
        field = side_a * side_b
        self.field = field
        circuit = 2 * side_a + 2 * side_b
        self.circuit = circuit

    @classmethod
    def is_it_square(cls, colour, side_a, side_b):

        if side_a == side_b:
            print(f'This is {colour} square')
        else:
            print(f'This is {colour} rectangle')

    @classmethod
    def create_Square_from_user_input(cls, colour, side_a, side_b):
        return cls.Square(colour, side_a, side_b)

    @property
    def square_field(self):
        return self.side_a * self.side_b

class Triangle(Square):

    def __init__(self, colour, side_a, side_b, side_c, height):
        super().__init__(colour, side_a, side_b)
        self.side_c = side_c
        self.height = height
        p = 0.5 * (side_a + side_b + side_c)
        field = 0.5 * side_a
        Heron_field = (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5
        self.Heron_field = Heron_field
        self.field = field
        circuit = side_a + side_b + side_c
        self.circuit = circuit


    @classmethod
    def create_Triangle_from_user_input(cls,colour, side_a, side_b, side_c, height):
        return cls.Triangle(colour, side_a, side_b, side_c, height)

class Circle:

    Pi = 3.14

    def __init__(self, colour, r):
        self.colour = colour
        self.r = r
        field = Circle.Pi * r ** 2
        self.field = field
        circuit = 2 * Circle.Pi * r
        self.circuit = circuit

    @classmethod
    def create_Circle_from_user_input(cls, colour, r):
        return cls.Circle(colour, r)

class Trapeze(Square):

    def __init__(self, colour, side_a, side_b, side_c, side_d, height):
        super().__init__(colour, side_a, side_b)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d
        self.height = height
        field = 0.5 * (side_a + side_b) * height
        self.field = field
        circuit = side_a + side_b + side_c + side_d
        self.circuit = circuit

    @classmethod
    def create_Trapeze_from_user_input(cls,colour, side_a, side_b, side_c, side_d, height):
        return Trapeze(colour, side_a, side_b, side_c, side_d, height)

    @property
    def Trapeze_field(self):
        return 0.5 * (self.side_a + self.side_b) * self.height

class Rhombus(Figure):

    def __init__(self, colour, side_a, height):
        super().__init__(colour)
        self.side_a = side_a
        self.height = height
        field = side_a * height
        self.field = field
        circuit = 4 * side_a
        self.circuit = circuit

    @classmethod
    def create_Rhombus_from_user_input(cls, colour, side_a, height):
        return cls.Rhombus(colour, side_a, height)

if __name__ == '__main__':

    s1 = Square('Green', 2, 2)
    s2 = Square('Red', 2, 3)
    s3 = Square('White', 3, 3)
    t1 = Triangle('Green', 2, 3, 4, 3)
    t2 = Triangle('Orange', 5, 2, 3, 6)
    t3 = Triangle('Black', 3, 4, 7, 5)
    c1 = Circle('Red', 3)
    c2 = Circle('Blue', 4)
    c3 = Circle('Orange', 5)
    tra1 = Trapeze('White', 1, 5, 7, 2, 4)
    tra2 = Trapeze('Black', 4, 3, 2, 5, 3)
    tra3 = Trapeze('Red', 2, 5, 4, 3, 7)
    rho1 = Rhombus('Yellow', 3, 2)
    rho2 = Rhombus('Red', 3, 4)
    rho3 = Rhombus('Blue', 3, 6)

    all_figure = [s1, s2, s3, t1, t2, t3, c1, c2, c3, tra1, tra2, tra3, rho1, rho2, rho3]

    print(all_figure)

    print(all_figure[0])

    print(s1.field)

    print(s2.colour)

    print(s3.circuit)

    print(t1.field)

    print(t2.colour)

    print(t3.circuit)

    print(c1.field)

    print(c2.colour)

    print(c3.circuit)

    print(tra1.field)

    print(tra2.colour)

    print(tra3.circuit)

    print(rho1.field)

    print(rho2.colour)

    print(rho3.circuit)

    Square.is_it_square('White', 2, 3)

    Square.is_it_square('Red', 4, 4)