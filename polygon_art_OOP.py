import turtle
import random


class PolygonDrawer:
    def __init__(self, reduction_ratio=0.618):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        self.reduction_ratio = reduction_ratio

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        self.turtle.penup()
        self.turtle.goto(location[0], location[1])
        self.turtle.setheading(orientation)
        self.turtle.color(color)
        self.turtle.pensize(border_size)
        self.turtle.pendown()

        for _ in range(num_sides):
            self.turtle.forward(size)
            self.turtle.left(360 / num_sides)

        self.turtle.penup()

    @staticmethod
    def get_new_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_random_polygons(self, count=20):
        for _ in range(count):
            num_sides = random.randint(3, 5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)

            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
            self.draw_inner_polygon(num_sides, size, orientation, location, color, border_size)

    def draw_inner_polygon(self, num_sides, size, orientation, location, color, border_size):
        size *= self.reduction_ratio
        self.turtle.penup()
        self.turtle.goto(location[0], location[1])
        self.turtle.forward(size * (1 - self.reduction_ratio) / 2)
        self.turtle.left(90)
        self.turtle.forward(size * (1 - self.reduction_ratio) / 2)
        self.turtle.right(90)

        new_location = [self.turtle.xcor(), self.turtle.ycor()]

        self.draw_polygon(num_sides, size, orientation, new_location, color, border_size)

    def hold_window(self):
        turtle.done()


# Usage
polygon_drawer = PolygonDrawer()
polygon_drawer.draw_random_polygons()
polygon_drawer.hold_window()
