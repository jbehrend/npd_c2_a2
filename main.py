'''Contains shape classes and does fun things with them

Shapes:
Triangle
Square
Circle

Data Attributes:
shape_type
edge_length
name
allies
enemies

Methods:
area
perimeter
update_edge_length
add_ally
add_enemy
'''

import math

class Square(object):
    shape_type = 'square'

    def __init__(self, edge_length, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return self.edge_length**2

    def perimeter(self):
        return self.edge_length * 4

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

class Triangle(object):
    shape_type = 'triangle'

    def __init__(self, edge_length, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return ((3^0.5)/4) * self.edge_length * self.edge_length

    def perimeter(self):
        return self.edge_length * 4

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

class Circle(object):
    shape_type = 'circle'

    def __init__(self, radius, name, allies, enemies):
        self.radius = radius
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return math.pi * self.radius * self.radius

    def update_radius(self, new_radius):
        self.radius = new_radius

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

if __name__ == '__main__':
    square_marty = Square(5, "marty", [], [])
    square_cynthia = Square(2.5, "cynthia", [], [])

    triangle_joe = Triangle(3, "joe", ["shirley", "susan"], ["marty", "cynthia"])
    triangle_jim = Triangle(6, "jim", ["shirley", "susan"], ["marty", "cynthia"])

    circle_susan = Circle(2, "susan", ["marty", "joe"], ["marty", "cynthia"])
    circle_shirley = Circle(3.5, "shirley", ["marty", "joe"], ["marty", "cynthia"])


    flatland = [triangle_joe, triangle_jim, circle_susan, circle_shirley, square_marty, square_cynthia]

    for person in flatland:
        print("Name: {} Type: {} Friends: {} Enemies{}".format(person.name,
                                                               person.shape_type,
                                                               person.allies,
                                                               person.enemies))
